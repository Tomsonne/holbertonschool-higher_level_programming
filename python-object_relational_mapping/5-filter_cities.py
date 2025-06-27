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

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()

    sql = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """

    cur.execute(sql, (sys.argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
