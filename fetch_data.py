#!/usr/bin/python

import argparse
from pprint import pprint

import os
import sqlite3

import dbs

def create_sqlite_file(file_name):
    (conn, cursor) = dbs.connect_mysql()

    new_sqlite_cursor = sqlite3.connect(file_name)

    table_names = dbs.get_name_of_tables_mysql(cursor)

    for table_name in table_names:
        sql = dbs.get_create_table_mysql(cursor, table_name)
        new_sqlite_cursor.execute(sql)

def copy_data(cur_mysql, new_sqlite, serverPersonId, name_of_table):
    cur_mysql.execute("SELECT * FROM %s WHERE serverPersonId = %s" % (name_of_table, serverPersonId))

    for row in cur_mysql.fetchall():
        insert = dbs.tuple_to_insert(name_of_table, row)

        new_sqlite.execute(insert)

    new_sqlite.commit()

def populates_sqlite_file(file_name, person_id):
    (db_mysql, cur_mysql) = dbs.connect_mysql()
    (db_sqlite, cur_sqlite) = dbs.connect_sqlite()

    name_of_tables = dbs.get_name_of_tables_mysql(cur_mysql)

    new_sqlite = sqlite3.connect(file_name)

    for name_of_table in name_of_tables:
        copy_data(cur_mysql, new_sqlite, person_id, name_of_table)

def main(file_name, person_id):
    if os.path.isfile(file_name):
        os.remove(file_name)

    create_sqlite_file(file_name)

    populates_sqlite_file(file_name, person_id)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("sqlite_file", type=str, help="File to save the data")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--server-person-id [PERSON-ID]", dest='server_person_id', type=int)
    group.add_argument("--group-id [GROUP_ID]", dest='group_id', type=int)


    args = parser.parse_args()

    main(args.sqlite_file, args.server_person_id)
