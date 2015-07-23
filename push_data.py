#!/usr/bin/python

import dbs

serverPersonId = 1

# whitelisted_tables = []

def get_name_of_tables(cur_sqlite):
    cur_sqlite.execute("SELECT name FROM sqlite_master WHERE type='table'")

    tables = []

    for table in cur_sqlite.fetchall():
        tables.append(table[0])

    return tables

def main():
    (db_mysql, cur_mysql) = dbs.connect_mysql()
    (db_sqlite, cur_sqlite) = dbs.connect_sqlite()

    sqlite_tables = get_name_of_tables(cur_sqlite)

    for table in sqlite_tables:
        results = cur_sqlite.execute("SELECT * FROM " + table)

        insert = "INSERT INTO table "
        for row in results.fetchall():
            str_row = []
            for r in row:
                str_row.append(str(r))

            print ",".join(str_row)

if __name__ == '__main__':
    main()
