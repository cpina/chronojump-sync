#!/usr/bin/python

import dbs

def drop_chronojump_table(db_mysql, cur_mysql):
    cur_mysql.execute("DROP DATABASE chronojump")
    cur_mysql.execute("CREATE DATABASE chronojump")

def add_person_id(sql):
    sql = sql.replace(" (", "( serverPersonId INT, ")
    return sql

def main():
    (db_mysql, cur_mysql) = dbs.connect_mysql()
    (db_sqlite, cur_sqlite) = dbs.connect_sqlite()

    drop_chronojump_table(db_mysql, cur_mysql)
    (db_mysql, cur_mysql) = dbs.connect_mysql()

    # Creates tables
    table_names = dbs.get_name_of_tables(cur_sqlite)

    for table_name in table_names:
        sql_table = dbs.get_create_table(cur_sqlite, table_name)
        sql_table = add_person_id(sql_table)

        cur_mysql.execute(sql_table)

if __name__ == '__main__':
    main()
