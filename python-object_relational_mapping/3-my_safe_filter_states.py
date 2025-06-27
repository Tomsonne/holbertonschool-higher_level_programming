#!/usr/bin/python3
""""
popo
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """"
    popo
    """
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()

    query = ("SELECT * FROM states WHERE name = %s "
             "ORDER BY id ASC;")
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
