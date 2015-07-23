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

def get_name_of_tables(cur_sqlite):
    cur_sqlite.execute("SELECT name FROM sqlite_master WHERE type='table'")

    tables = []

    for table in cur_sqlite.fetchall():
        tables.append(table[0])

    return tables

def get_create_table(cur_sqlite, table_name):
    results = cur_sqlite.execute("select sql from sqlite_master where type = 'table' and name = '%s'" % table_name)
    return results.fetchall()[0][0]
