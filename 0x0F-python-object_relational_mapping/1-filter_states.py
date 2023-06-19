#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user='root',
                         passwd='root', db='hbtn_0e_0_usa', port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id")
    rows = cur.fetchall()
    for _ in rows:
        print(_)
    cur.close()
    db.close()
