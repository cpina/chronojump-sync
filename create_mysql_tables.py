#!/usr/bin/python

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

def drop_chronojump_table(db_mysql, cur_mysql):
    cur_mysql.execute("DROP DATABASE chronojump")
    cur_mysql.execute("CREATE DATABASE chronojump")

def main():
    (db_mysql, cur_mysql) = connect_mysql()
    (db_sqlite, cur_sqlite) = connect_sqlite()

    drop_chronojump_table(db_mysql, cur_mysql)

    (db_mysql, cur_mysql) = connect_mysql()

    cur_sqlite.execute("SELECT sql FROM sqlite_master WHERE type='table'")

    for sql_table in cur_sqlite.fetchall():
        sql_table = sql_table[0]

        cur_mysql.execute(sql_table)

if __name__ == '__main__':
    main()