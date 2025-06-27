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
    state_name = sys.argv[4]
    
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()

    sql = ("SELECT * FROM states WHERE name LIKE BINARY '{}' "
           "ORDER BY states.id ASC;".format(state_name))
    
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
