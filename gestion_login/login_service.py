import logging
from flask import Flask, request, jsonify
import pybreaker
import redis  # Cliente de Redis
import bcrypt  # Para hashear las contraseñas
# from flask_cors import CORS  # Importar CORS desde flask_cors

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Configuración del Circuit Breaker
login_circuit = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=30)

# Configuración de Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Crear la aplicación Flask
app = Flask(__name__)

# Habilitar CORS
# CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Listener personalizado para el Circuit Breaker
class LoginCircuitBreakerListener(pybreaker.CircuitBreakerListener):
    def before_call(self, circuit_breaker, func, *args, **kwargs):
        logging.info(f"Antes de llamar a la función {func.__name__} con los argumentos {args}")

    def on_call_success(self, circuit_breaker, func, *args, **kwargs):
        logging.info(f"La llamada a la función {func.__name__} fue exitosa")

    def on_call_failure(self, circuit_breaker, func, *args, **kwargs):
        logging.warning(f"La llamada a la función {func.__name__} falló")

    def on_open(self, circuit_breaker, *args, **kwargs):
        logging.warning("El Circuit Breaker está en estado abierto (Open)")

    def on_half_open(self, circuit_breaker, *args, **kwargs):
        logging.info("El Circuit Breaker está en estado medio abierto (Half-Open)")

    def on_close(self, circuit_breaker, *args, **kwargs):
        logging.info("El Circuit Breaker está en estado cerrado (Closed)")

# Agregar el listener al Circuit Breaker
login_circuit.add_listener(LoginCircuitBreakerListener())

def hash_password(password):
    """Hashea la contraseña antes de guardarla."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_credentials_to_redis(username, password):
    """Guarda las credenciales (hasheadas) en Redis."""
    hashed_password = hash_password(password)
    redis_client.set(username, hashed_password)
    logging.info(f"Credenciales guardadas en Redis para el usuario: {username}")

def is_valid_login(username, password):
    """Verifica las credenciales desde Redis (comparando contraseñas hasheadas)."""
    stored_password_hash = redis_client.get(username)
    if stored_password_hash and bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
        return True
    raise Exception("Login fallido: credenciales incorrectas")  # Simula un fallo

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"message": "Usuario y contraseña son obligatorios"}), 400

    save_credentials_to_redis(username, password)
    return jsonify({"message": "Usuario registrado correctamente"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    logging.info(f"Estado del Circuit Breaker antes de la llamada: {login_circuit.state}")
    
    if login_circuit.state == pybreaker.STATE_OPEN:
        logging.error("El Circuit Breaker está en estado abierto (Open), rechazando la solicitud.")
        return jsonify({"message": "Servicio temporalmente no disponible"}), 503

    try:
        result = login_circuit.call(is_valid_login, username, password)
        
        if result:
            logging.info(f"Login exitoso para {username}")
            return jsonify({"message": "Login exitoso"}), 200
        else:
            logging.warning(f"Login fallido para {username}")
            return jsonify({"message": "Credenciales incorrectas"}), 401
    
    except pybreaker.CircuitBreakerError:
        logging.error("El Circuit Breaker se ha activado debido a múltiples fallos.")
        return jsonify({"message": "Servicio temporalmente no disponible"}), 503
    except Exception as e:
        logging.error(f"Error inesperado: {str(e)}")
        return jsonify({"message": "Credenciales incorrectas"}), 401

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9002)
