from flask import Flask, request
from flask_graphql import GraphQLView
import requests
import graphene

app = Flask(__name__)


# Define GraphQL query schema
class Query(graphene.ObjectType):
    users = graphene.List(graphene.String)
    user = graphene.Field(graphene.String, id=graphene.Int())
    doctors = graphene.List(graphene.String)
    patients = graphene.List(graphene.String)

    def resolve_users(self, info):
        # Example of body { "query": "{ users }" }
        try:
            response = requests.get('http://localhost:8000/app/api/v1/app/')
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching users: {e}")
            return ["Error fetching users"]

    def resolve_user(self, info, id):
        # Example of body { "query": "{ user(id: <id>) }" }
        try:
            response = requests.get(f'http://localhost:8000/app/api/v1/app/{id}/')
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching user: {e}")
            return "Error fetching user"

    def resolve_doctors(self, info):
        # Example of body { "query": "{ doctors }" }
        try:
            response = requests.get('http://localhost:8000/app/api/v1/app/doctors/')
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching doctors: {e}")
            return ["Error fetching doctors"]

    def resolve_patients(self, info):
        # Example of body { "query": "{ patients }" }
        try:
            response = requests.get('http://localhost:8000/app/api/v1/app/pacientes/')
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching patients: {e}")
            return ["Error fetching patients"]



# Define authentication and context handling
def verify_token(token):
    try:
        response = requests.post('http://authservice-service/verify-token', json={'token': token})
        data = response.json()
        if data.get('isValid', False):
            return token
        else:
            raise Exception("Token is invalid")
    except Exception as e:
        raise Exception("Error validating token") from e

# @app.before_request
# def check_auth():
#     auth_header = request.headers.get('Authorization', '')
#     token = auth_header.split('Bearer ')[-1]
#     if not token or not verify_token(token):
#         return "Unauthorized", 401

# Setup GraphQL view
schema = graphene.Schema(query=Query)

app.add_url_rule(
    '/', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True)
