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

def copy_data(cur_mysql, new_sqlite, serverPersonId, name_of_table):
    cur_mysql.execute("SELECT * FROM %s WHERE serverPersonId = %s" % (name_of_table, serverPersonId))

    for row in cur_mysql.fetchall():
        insert = dbs.tuple_to_insert(name_of_table, row)
        
        print insert
        new_sqlite.execute(insert)

    new_sqlite.commit()

def populates_sqlite_file(file_name):
    (db_mysql, cur_mysql) = dbs.connect_mysql()
    (db_sqlite, cur_sqlite) = dbs.connect_sqlite()

    name_of_tables = dbs.get_name_of_tables(cur_sqlite)

    new_sqlite = sqlite3.connect(file_name)

    for name_of_table in name_of_tables:
        copy_data(cur_mysql, new_sqlite, serverPersonId, name_of_table)

def main():
    file_name="test.db"

    if os.path.isfile(file_name):
        os.remove(file_name)

    create_sqlite_file(file_name)

    populates_sqlite_file(file_name)

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
