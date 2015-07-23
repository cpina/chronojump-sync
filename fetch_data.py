#!/usr/bin/python

import os
import sqlite3

import dbs

serverPersonId = "1"

def create_sqlite_file(file_name):
    (conn, cursor) = dbs.connect_sqlite()

    new_sqlite_cursor = sqlite3.connect(file_name)

    table_names = dbs.get_name_of_tables(cursor)

    for table_name in table_names:
        sql = dbs.get_create_table(cursor, table_name)
        new_sqlite_cursor.execute(sql)

def get_name_of_tables(cur_sqlite):
    cur_sqlite.execute("SELECT name FROM sqlite_master WHERE type='table'")

    tables = []

    for table in cur_sqlite.fetchall():
        tables.append(table[0])

    return tables

def main():
    file_name="test.db"
    if os.path.isfile(file_name):
        os.remove("test.db")

    create_sqlite_file("test.db")
"""
    (db_mysql, cur_mysql) = dbs.connect_mysql()
    (db_sqlite, cur_sqlite) = dbs.connect_sqlite()

    sqlite_tables = get_name_of_tables(cur_sqlite)

    for table in sqlite_tables:
        results = cur_sqlite.execute("SELECT * FROM " + table)

        for row in results.fetchall():
            insert = "INSERT INTO " + table + " VALUES( " + serverPersonId + ", "
            str_row = []
            for r in row:
                str_row.append("'" + str(r).replace("'", "\\'") + "'")

            insert += ",".join(str_row)

            insert += ")"

            print insert
            cur_mysql.execute(insert)

    db_mysql.commit()
"""

if __name__ == '__main__':
    main()
