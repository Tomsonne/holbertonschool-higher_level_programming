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

# Route protégée par authentification basique
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# Route de connexion pour obtenir un token JWT
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()  # Récupération des données JSON envoyées
    username = data.get("username")
    password = data.get("password")

    # Vérification de l'existence de l'utilisateur et de son mot de passe
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Création du token JWT avec l'identité de l'utilisateur
    access_token = create_access_token(identity={
        "username": username,
        "role": user["role"]
    })
    return jsonify(access_token=access_token)

# Route protégée par token JWT
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Route protégée par token JWT avec vérification du rôle admin
@app.route("/admin-only")
@jwt_required()
def admin_only():
    identity = get_jwt_identity()  # Récupération des infos du token
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# Gestion personnalisée des erreurs liées à l'authentification JWT

# Erreur si le token est manquant
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

# Erreur si le token est invalide (signature, format, etc.)
@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

# Erreur si le token est expiré
@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

# Erreur si le token a été révoqué (non utilisé ici, mais prêt à l'emploi)
@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

# Erreur si un "fresh token" est requis (non utilisé ici)
@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

# Lancement de l'application Flask
if __name__ == "__main__":
    app.run()
