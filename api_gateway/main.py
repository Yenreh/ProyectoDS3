from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Microservice endpoints
users_microservice_endpoint = 'http://localhost:8000/app/api/v1/app/'
auth_microservice_endpoint = 'http://localhost:9002/login'  # The first app's login endpoint

@app.route('/login', methods=['POST'])
def login():
    # Obtaining login credentials from the request
    username = request.json.get('username')
    password = request.json.get('password')

    # Make a request to the login microservice
    try:
        login_response = requests.post(auth_microservice_endpoint, json={'username': username, 'password': password})
        
        if login_response.status_code == 200:
            return jsonify({"message": "Login successful", "data": login_response.json()}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error during login: {e}"}), 500


@app.route('/users', methods=['GET'])
def get_users():
    # Body = None
    try:
        response = requests.get(f'{users_microservice_endpoint}')
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching users: {e}")
        return jsonify({"error": "Error fetching users"}), 500


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


if __name__ == '__main__':
    app.run(debug=True)
