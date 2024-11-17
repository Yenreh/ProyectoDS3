from flask import Flask, jsonify, request
import requests
from flask_cors import CORS  # Importar CORS desde flask_cors
import time

app = Flask(__name__)


# Microservice endpoints
users_microservice_endpoint = 'http://gestion-usuarios-service:8000/app/api/v1/app/'
login_microservice_endpoint = 'http://localhost:9002/login'  # The first app's login endpoint
appointments_microservice_endpoint = 'http://gestion-citas-medicas-service:8000/api/'
auth_microservice_endpoint = 'http://auth-service:3000/'


CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Variables para simular el Circuit Breaker
login_failures = 0
LOGIN_FAILURE_THRESHOLD = 3
LOGIN_RESET_TIMEOUT = 30  # Segundos para resetear el "Circuit Breaker"
last_failure_time = 0


# Endpoints for Login Microservice

@app.route('/login', methods=['POST'])
def login():
    # Obtaining login credentials from the request
    username = request.json.get('username')
    password = request.json.get('password')
    
    global login_failures, last_failure_time

    # Verificar si el Circuit Breaker está abierto
    if login_failures >= LOGIN_FAILURE_THRESHOLD and time.time() - last_failure_time < LOGIN_RESET_TIMEOUT:
        return jsonify({"message": "Servicio temporalmente no disponible"}), 503

    # Make a request to the login microservice
    try:
        login_response = requests.post(login_microservice_endpoint, json={'username': username, 'password': password})
        
        if login_response.status_code == 200:
            login_failures = 0  # Resetear el contador de fallos en caso de éxito
            return jsonify({"message": "Login successful", "data": login_response.json()}), 200
        else:
            login_failures += 1
            last_failure_time = time.time()
            return jsonify({"message": "Invalid credentials"}), 401
    except requests.exceptions.RequestException as e:
        login_failures += 1
        last_failure_time = time.time()
        return jsonify({"error": f"Error during login: {e}"}), 500


# Endpoints for Users Microservice


@app.route('/users', methods=['GET'])
def get_users():
    try:
        response = requests.get(f'{users_microservice_endpoint}')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching users: {e}")
        return jsonify({"error": "Error fetching users"}), 500


@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    try:
        response = requests.get(f'{users_microservice_endpoint}{id}/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user: {e}")
        return jsonify({"error": "Error fetching user"}), 500


@app.route('/doctors', methods=['GET'])
def get_doctors():
    try:
        response = requests.get(f'{users_microservice_endpoint}doctors/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching doctors: {e}")
        return jsonify({"error": "Error fetching doctors"}), 500


@app.route('/patients', methods=['GET'])
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
def create_user():
    try:
        user_data = request.get_json()  # Assuming the user data is sent in the body as JSON
        response = requests.post(f'{users_microservice_endpoint}', json=user_data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error creating user: {e}")
        return jsonify({"error": "Error creating user"}), 500


@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user_data = request.get_json()  # Assuming the user data is sent in the body as JSON
        response = requests.put(f'{users_microservice_endpoint}{id}/', json=user_data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error updating user: {e}")
        return jsonify({"error": "Error updating user"}), 500


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        response = requests.delete(f'{users_microservice_endpoint}{id}/')
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error deleting user: {e}")
        return jsonify({"error": "Error deleting user"}), 500


# Endpoints for Appointments Microservice


@app.route('/transactions_appointments', methods=['GET'])
def get_transactions_appointments():
    # Body = None
    try:
        response = requests.get(f'{appointments_microservice_endpoint}transactions/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transactions: {e}")
        return jsonify({"error": "Error fetching transactions"}), 500


@app.route('/appointments', methods=['GET'])
def get_appointments():
    # Body = None
    try:
        response = requests.get(f'{appointments_microservice_endpoint}appointments/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching appointments: {e}")
        return jsonify({"error": "Error fetching appointments"}), 500


@app.route('/appointment/create', methods=['POST'])
def create_appointment():
    # Body = JSON
    # {
    #     "patient_id": 1,
    #     "doctor_id": 1,
    #     "date_time": "2021-07-01T10:00:00"
    # }
    try:
        appointment_data = request.get_json()  # Assuming the appointment data is sent in the body as JSON
        response = requests.post(f'{appointments_microservice_endpoint}appointments/', json=appointment_data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error creating appointment: {e}")
        return jsonify({"error": "Error creating appointment"}), 500


@app.route('/appointment/update', methods=['PUT'])
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


# Endpoints for Auth Microservice

# Define authentication and context handling
def verify_token(token):
    try:
        response = requests.post(f'{auth_microservice_endpoint}verify-token', json={'token': token})
        data = response.json()
        if data.get('isValid', False):
            return token
        else:
            raise Exception("Token is invalid")
    except Exception as e:
        raise Exception("Error validating token") from e


@app.before_request
def check_auth():
    auth_header = request.headers.get('Authorization', '')
    token = auth_header.split('Bearer ')[-1]
    if not token or not verify_token(token):
        return jsonify({"error": "Unauthorized"}), 401


if __name__ == '__main__':
    app.run(debug=True, port=5000)
