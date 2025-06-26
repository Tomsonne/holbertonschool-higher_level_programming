#!/Users/thomasrousseau/Documents/Projets/holbertonschool-hbnb/.venv/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    
    # Connexion à MySQL
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    
    # Création du curseur et exécution de la requête
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Récupération et affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Fermeture
    cur.close()
    db.close()
