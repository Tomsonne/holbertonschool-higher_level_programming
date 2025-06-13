from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

# Création de l'application Flask
app = Flask(__name__)

# Initialisation de l'authentification basique
auth = HTTPBasicAuth()

# Configuration de la clé secrète utilisée pour sécuriser les tokens JWT
app.config["JWT_SECRET_KEY"] = "ma_cle_secrete_super_secure"

# Initialisation de la gestion JWT
jwt = JWTManager(app)

# Dictionnaire contenant les utilisateurs en mémoire
# Chaque utilisateur a un nom, un mot de passe haché et un rôle
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),  # Hachage sécurisé
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Fonction de vérification des identifiants pour l'authentification basique
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username  # L'utilisateur est authentifié
    return None

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected(username, password):
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()  # Récupération des données JSON envoyées
    username = data.get("username") #prend la data json correspondante a username
    password = data.get("password") #fait pareil
    user = users.get(username)

    if user is not None:
        if verify_password(username, password) is not None:
            jwt = create_access_token(identity=username)
            res = {"access_token": jwt}
            return jsonify(res)
    
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/jwt-protected") # Prend methods GET quand même 
@jwt_required() #protege la route
def jwt_protected():
    return ({"error": "Missing or invalid token"})

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()  
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"
