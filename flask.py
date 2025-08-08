from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json()
    users.append(user)
    return jsonify({"message": "User added"}), 201

@app.route('/users/<int:index>', methods=['PUT'])
def update_user(index):
    if index < 0 or index >= len(users):
        return jsonify({"error": "User not found"}), 404
    users[index] = request.get_json()
    return jsonify({"message": "User updated"}) 

@app.route('/users/<int:index>', methods=['DELETE'])
def delete_user(index):
    if index < 0 or index >= len(users):
        return jsonify({"error": "User not found"}), 404
    users.pop(index)
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)