import MySQLdb
import sqlite3

def connect_sqlite():
    conn = sqlite3.connect('Chronojump/database/chronojump.db')

    return (conn, conn.cursor())

def connect_mysql():
    conn = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='tissues',
        db='chronojump'
        )

    return (conn, conn.cursor())

