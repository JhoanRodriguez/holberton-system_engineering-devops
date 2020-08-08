#!/usr/bin/python3
"""
Script will display states sorted by id in ascending order
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
