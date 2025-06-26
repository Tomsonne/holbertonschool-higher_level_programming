import MySQLdb
from sqlalchemy import create_engine, text

# Configuration de connexion
HOST = "localhost"
USER = "root"           # ou un autre utilisateur MySQL
PASSWORD = "19mE9Bhe"  # Remplace par ton mot de passe MySQL
DATABASE = "test_db"

# 🔵 Test avec MySQLdb
print("=== Test avec MySQLdb ===")
try:
    conn = MySQLdb.connect(
        host=HOST,
        user=USER,
        passwd=PASSWORD,
        db=DATABASE
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    for row in rows:
        print(f"MySQLdb - Utilisateur : {row[1]}")
    conn.close()
except Exception as e:
    print(f"MySQLdb - Erreur : {e}")

# 🔶 Test avec SQLAlchemy
print("\n=== Test avec SQLAlchemy ===")
try:
    engine = create_engine(f"mysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}")
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM users;"))
        for row in result:
            print(f"SQLAlchemy - Utilisateur : {row.name}")
except Exception as e:
    print(f"SQLAlchemy - Erreur : {e}")
