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
    cur_sqlite.execute("SELECT sql FROM sqlite_master WHERE type='table'")

    for sql_table in cur_sqlite.fetchall():
        sql_table = add_person_id(sql_table[0])
        print sql_table

        cur_mysql.execute(sql_table)

if __name__ == '__main__':
    main()
