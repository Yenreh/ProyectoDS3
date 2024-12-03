from flask import Flask, jsonify, request, session
import requests
from flask_cors import CORS
from functools import wraps
from dotenv import load_dotenv 
import os
# Cargar variables de entorno desde el archivo .env
load_dotenv()
app = Flask(__name__)
CORS(app)
app.secret_key = 'mi_clave_secreta'  # Necesario para usar sesiones en Flask



# Endpoints de los microservicios
users_microservice_endpoint = 'http://localhost:8000/app/api/v1/app/'
appointments_microservice_endpoint = 'http://localhost:8001/api/'

# Endpoint de autenticación
auth_service_endpoint = 'http://localhost:3000/auth/login'
firebase_token_validation_endpoint = f"https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={os.getenv('FIREBASE_API_KEY')}"
logout_service_endpoint = 'http://localhost:3000/auth/logout'  # El endpoint de logout

# Middleware de autenticación
def auth_required(f):
    @wraps(f)
    def wrapped_function(*args, **kwargs):
        # Verificar si el token de autorización está presente en la sesión
        token = session.get('auth_token')
        if not token:
            return jsonify({"error": "Token de autorización no proporcionado"}), 401
        
        try:
            # Enviar token al servicio de autenticación para validarlo
            print(f"Token enviado para validación: {token}")  # Depuración
            response = requests.post(firebase_token_validation_endpoint, json={'idToken': token})
            if response.status_code != 200:
                print(f"Error de validación de token: {response.status_code} - {response.text}")  # Depuración
                return jsonify({"error": "Token inválido o no autorizado"}), 401
            
            # Si el token es válido, puedes acceder a los datos del usuario
            request.user = response.json()  # Información del usuario autenticado
        except requests.exceptions.RequestException as e:
            print(f"Error al validar token: {e}")
            return jsonify({"error": "Error al validar token"}), 500
        
        return f(*args, **kwargs)
    return wrapped_function

# Endpoint para autenticarse con el servicio de autenticación y guardar el token
@app.route('/auth/login', methods=['POST'])
def login():
    try:
        # Obtener las credenciales del cuerpo de la solicitud
        email = request.json.get('email')
        password = request.json.get('password')
        
        if not email or not password:
            return jsonify({"error": "Correo o contraseña faltante"}), 400
        
        # Hacer una solicitud POST al servicio de autenticación con el correo y la contraseña
        response = requests.post(auth_service_endpoint, json={'email': email, 'password': password})
        
        if response.status_code == 200:
            # Si la autenticación es exitosa, guarda el token en la sesión
            data = response.json()
            print(f"Respuesta de autenticación: {data}")  # Ver el contenido de la respuesta
            # Guardar el accessToken en la sesión
            session['auth_token'] = data['user']['stsTokenManager']['accessToken']  # Guarda el accessToken
            print(f"Token guardado en la sesión: {session.get('auth_token')}")  # Depuración
            return jsonify(data), 200  # Aquí devuelves la respuesta del servicio de autenticación
        else:
            return jsonify({"error": "Error de autenticación"}), 401
        
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return jsonify({"error": "Error al iniciar sesión"}), 500

# Endpoint de logout (destruye la sesión y llama al servicio de logout externo)
@app.route('/auth/logout', methods=['POST'])
def logout():
    try:
        # Obtener el token de la sesión (si está presente)
        token = session.get('auth_token')
        if not token:
            return jsonify({"message": "No hay sesión activa"}), 400
        
        # Hacer la solicitud al servicio de logout en el servidor de autenticación
        response = requests.post(logout_service_endpoint, headers={"Authorization": f"Bearer {token}"})
        
        if response.status_code == 200:
            # Si la solicitud al servicio de logout es exitosa, destruir el token de la sesión
            session.pop('auth_token', None)  # Eliminar el token de la sesión
            return jsonify({"message": "Sesión cerrada correctamente"}), 200
        else:
            return jsonify({"message": "Error al cerrar sesión en el servicio de autenticación"}), 500
    except Exception as e:
        print(f"Error al cerrar sesión: {e}")
        return jsonify({"message": "Error al cerrar sesión"}), 500

# Endpoints para el Microservicio de Usuarios
@app.route('/users', methods=['GET'])
@auth_required
def get_users():
    # Body = None
    try:
        # Solicitar datos de usuarios al microservicio
        response = requests.get(f'{users_microservice_endpoint}')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching users: {e}")
        return jsonify({"error": "Error fetching users"}), 500

@app.route('/user/<int:id>', methods=['GET'])
@auth_required
def get_user(id):
    # Body = None
    try:
        # Solicitar datos de un usuario específico
        response = requests.get(f'{users_microservice_endpoint}{id}/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user: {e}")
        return jsonify({"error": "Error fetching user"}), 500


@app.route('/doctors', methods=['GET'])
@auth_required
def get_doctors():
    # Body = None
    try:
        response = requests.get(f'{users_microservice_endpoint}doctors/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching doctors: {e}")
        return jsonify({"error": "Error fetching doctors"}), 500    

@app.route('/patients', methods=['GET'])
@auth_required
def get_patients():
    try:
        response = requests.get(f'{users_microservice_endpoint}pacientes/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching patients: {e}")
        return jsonify({"error": "Error fetching patients"}), 500

# Add POST, PUT, DELETE for user operations
@app.route('/user', methods=['POST'])
@auth_required
def create_user():
     # Body = JSON
    # {
    #     "id": 1,
    #     "cc_user": 123456789,
    #     "user_type": "paciente",
    #     "name": "John Doe",
    #     "date_of_birth": "1990-01-01",
    #     "professional_id": "PROF12345",
    #     "password": "password123",
    #     "email": "johndoe@example.com",
    #     "phone": "123-456-7890"
    # }
    try:
        # Crear un nuevo usuario
        user_data = request.get_json()
        response = requests.post(f'{users_microservice_endpoint}', json=user_data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error creating user: {e}")
        return jsonify({"error": "Error creating user"}), 500

@app.route('/user/<int:id>', methods=['PUT'])
@auth_required
def update_user(id):
    # Body = JSON
    # {
    #     "cc_user": 987654321,
    #     "user_type": "doctor",
    #     "name": "Dr. Jane Updated",
    #     "date_of_birth": "1985-06-15",
    #     "professional_id": "PROF67890",
    #     "password": "newpassword123",
    #     "email": "drjaneupdated@example.com",
    #     "phone": "987-654-3210"
    # }
    try:
        user_data = request.get_json()  # Assuming the user data is sent in the body as JSON
        response = requests.put(f'{users_microservice_endpoint}{id}/', json=user_data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error updating user: {e}")
        return jsonify({"error": "Error updating user"}), 500



@app.route('/user/<int:id>', methods=['DELETE'])
@auth_required
def delete_user(id):
    # Body = None
    try:
        response = requests.delete(f'{users_microservice_endpoint}{id}/')
        if response.status_code == 204:
            return jsonify({"message": "User deleted successfully"}), 200
    except requests.exceptions.RequestException as e:
        print(f"Error deleting user: {e}")
        return jsonify({"error": "Error deleting user"}), 500
    

# Endpoints for Appointments Microservice
    
@app.route('/transactions_appointments', methods=['GET'])
@auth_required
def get_transactions_appointments():
    # Body = None
    try:
        response = requests.get(f'{appointments_microservice_endpoint}transactions/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transactions: {e}")
        return jsonify({"error": "Error fetching transactions"}), 500


# Endpoints para el Microservicio de Citas
@app.route('/appointments', methods=['GET'])
@auth_required
def get_appointments():
    try:
        # Solicitar datos de citas al microservicio
        response = requests.get(f'{appointments_microservice_endpoint}')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching appointments: {e}")
        return jsonify({"error": "Error fetching appointments"}), 500
    
@app.route('/appointment/create', methods=['POST'])
@auth_required
def create_appointment():
    # Body = JSON
    # {
    #     "patient_id": 1,
    #     "doctor_id": 1,
    #     "date_time": "2021-07-01T10:00:00"
    # }
    try:
        appointment_data = request.get_json()  # Assuming the appointment data is sent in the body as JSON
        response = requests.post(f'{appointments_microservice_endpoint}appointments/create/', json=appointment_data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error creating appointment: {e}")
        return jsonify({"error": "Error creating appointment"}), 500

@app.route('/appointment/update', methods=['PUT'])
@auth_required
def update_appointment():
    # Body = JSON
    # {
    #     "appointment_id": "a694e2f1-1731-4715-aac0-2d6e4fea49ec,
    #     "patient_id": 1,
    #     "doctor_id": 1,
    #     "status": "CONFIRMED"
    # }
    try:
        appointment_data = request.get_json()  # Assuming the appointment data is sent in the body as JSON
        data = {
            "patient_id": appointment_data.get("patient_id"),
            "doctor_id": appointment_data.get("doctor_id"),
            "status": appointment_data.get("status")
        }
        response = requests.put(f'{appointments_microservice_endpoint}appointments/{appointment_data.get("appointment_id")}/update/', json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error updating appointment: {e}")
        return jsonify({"error": "Error updating appointment"}), 500

@app.route('/appointment/delete', methods=['DELETE'])
@auth_required
def delete_appointment():
    # Body = JSON
    # {
    #     "appointment_id": "a694e2f1-1731-4715-aac0-2d6e4fea49ec
    # }
    try:
        appointment_data = request.get_json()  # Assuming the appointment data is sent in the body as JSON
        response = requests.delete(f'{appointments_microservice_endpoint}appointments/{appointment_data.get("appointment_id")}/delete/')
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error deleting appointment: {e}")
        return jsonify({"error": "Error deleting appointment"}), 500

@app.route('/appointments_history', methods=['GET'])
@auth_required
def get_appointment_history():
    # Body = None
    try:
        response = requests.get(f'{appointments_microservice_endpoint}appointment-history/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching appointment history: {e}")
        return jsonify({"error": "Error fetching appointment history"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
