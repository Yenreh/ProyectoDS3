from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Define RESTful routes for fetching users, doctors, and patients


@app.route('/users', methods=['GET'])
def get_users():
    # Body = None
    try:
        response = requests.get('http://localhost:8000/app/api/v1/app/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching users: {e}")
        return jsonify({"error": "Error fetching users"}), 500


@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    # Body = None
    try:
        response = requests.get(f'http://localhost:8000/app/api/v1/app/{id}/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user: {e}")
        return jsonify({"error": "Error fetching user"}), 500


@app.route('/doctors', methods=['GET'])
def get_doctors():
    # Body = None
    try:
        response = requests.get('http://localhost:8000/app/api/v1/app/doctors/')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching doctors: {e}")
        return jsonify({"error": "Error fetching doctors"}), 500


@app.route('/patients', methods=['GET'])
def get_patients():
    # Body = None
    try:
        response = requests.get('http://localhost:8000/app/api/v1/app/pacientes/')
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
        response = requests.post('http://localhost:8000/app/api/v1/app/', json=user_data)
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
        response = requests.put(f'http://localhost:8000/app/api/v1/app/{id}/', json=user_data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error updating user: {e}")
        return jsonify({"error": "Error updating user"}), 500


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    # Body = None
    try:
        response = requests.delete(f'http://localhost:8000/app/api/v1/app/{id}/')
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error deleting user: {e}")
        return jsonify({"error": "Error deleting user"}), 500


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
