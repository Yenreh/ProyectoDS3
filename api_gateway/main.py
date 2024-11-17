from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Define RESTful routes for fetching users, doctors, and patients

users_microservice_endpoint = 'http://localhost:8000/app/api/v1/app/'
appointments_microservice_endpoint = 'http://localhost:8001/api/'


# Endpoints for Users Microservice


@app.route('/users', methods=['GET'])
def get_users():
    # Body = None
    try:
        response = requests.get(f'{users_microservice_endpoint}')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching users: {e}")
        return jsonify({"": "Error fetchingerror users"}), 500


@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    # Body = None
    try:
        response = requests.get(f'{users_microservice_endpoint}{id}/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user: {e}")
        return jsonify({"error": "Error fetching user"}), 500


@app.route('/doctors', methods=['GET'])
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
def get_patients():
    # Body = None
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
        user_data = request.get_json()  # Assuming the user data is sent in the body as JSON
        response = requests.post(f'{users_microservice_endpoint}', json=user_data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error creating user: {e}")
        return jsonify({"error": "Error creating user"}), 500


@app.route('/user/<int:id>', methods=['PUT'])
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
def delete_user(id):
    # Body = None
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
        print(response.json())
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error deleting appointment: {e}")
        return jsonify({"error": "Error deleting appointment"}), 500
# Endpoints for Auth Microservice
# Define authentication and context handling
# def verify_token(token):
#     try:
#         response = requests.post('http://authservice-service/verify-token', json={'token': token})
#         data = response.json()
#         if data.get('isValid', False):
#             return token
#         else:
#             raise Exception("Token is invalid")
#     except Exception as e:
#         raise Exception("Error validating token") from e

# @app.before_request
# def check_auth():
#     auth_header = request.headers.get('Authorization', '')
#     token = auth_header.split('Bearer ')[-1]
#     if not token or not verify_token(token):
#         return jsonify({"error": "Unauthorized"}), 401


if __name__ == '__main__':
    app.run(debug=True)
