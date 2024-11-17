from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

# Redis connection
client = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

# Prepopulate valid tokens in Redis
valid_tokens = [
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMTEiLCJuYW1lIjoiQWxpY2UiLCJpYXQiOjE2MDIwMDAwMDB9.HaMtsRnsp4VvstGhJKymF_PnU1OUKkQBjYV6NajouIM",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMTIiLCJuYW1lIjoiQm9iIiwiaWF0IjoxNjAyMDAwMDAwfQ.aIYwb2EdEZFpI6yZKrqT7J4BvGf4v34zXOZ4Q3eAfa4",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMTMiLCJuYW1lIjoiQ2hhcmxpZSIsImlhdCI6MTYwMjAwMDAwMH0.1eX8y7t9I7uNAR2RTvmVNiZz-6T9ar4Bwh_vJZYmNOM",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMTQiLCJuYW1lIjoiRGFuYSIsImlhdCI6MTYwMjAwMDAwMH0.KOAz5z8l_J8gB4rWkIpb6nArKsFfGgM59H-QTYJqB_4",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMTUiLCJuYW1lIjoiRWRnYXIiLCJpYXQiOjE2MDIwMDAwMDB9.rFtw4nGnq7-0o1OhpPCsw5MlN-Rr9m-nn29f3ROG4Kk"
]

for token in valid_tokens:
    client.set(token, "valid", ex=86400)  # Set tokens with a 24-hour expiration
print("Tokens stored in Redis")


# Route to verify if a token is valid
@app.route('/verify-token', methods=['POST'])
def verify_token():
    data = request.json
    token = data.get('token')

    if not token:
        return jsonify({"error": "Token not provided."}), 400

    try:
        result = client.get(token)
        if result == "valid":
            return jsonify({"isValid": True}), 200
        else:
            return jsonify({"isValid": False}), 200
    except redis.RedisError as e:
        print("Error connecting to Redis:", e)
        return jsonify({"error": "Internal server error."}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
