from flask import Flask, jsonify, request

# Création de l’application Flask
app = Flask(__name__)

# Dictionnaire en mémoire qui stocke les utilisateurs
users = {}

# 1. Route principale
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# 2. Route /data : renvoie une liste des usernames
@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

# 3. Route /status : simple vérification de disponibilité
@app.route('/status')
def status():
    return "OK"

# 4. Route dynamique : /users/<username>
@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

# 5. Route POST pour ajouter un utilisateur
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    # Vérifie que 'username' est présent dans la requête
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

# Exécution du serveur Flask en local
if __name__ == '__main__':
    app.run()

