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
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    val = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(val)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
