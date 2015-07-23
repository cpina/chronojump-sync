#!/usr/bin/python

import dbs

import argparse

def main(sqlite_file, server_person_id):
    (db_mysql, cur_mysql) = dbs.connect_mysql()
    (db_sqlite, cur_sqlite) = dbs.connect_sqlite(sqlite_file)

    sqlite_tables = dbs.get_name_of_tables_sqlite(cur_sqlite)

    for table in sqlite_tables:
        results = cur_sqlite.execute("SELECT * FROM " + table)

        for row in results.fetchall():
            insert = "INSERT INTO " + table + " VALUES( " + server_person_id + ", "
            str_row = []
            for r in row:
                r = str(r).replace("'", '')
                str_row.append("'" + r + "'")
                #str_row.append("'" + str(r).replace("'", "\\'") + "'")

            insert += ",".join(str_row)

            insert += ")"

            cur_mysql.execute(insert)

    db_mysql.commit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("sqlite_file", type=str, help="File to upload")
    parser.add_argument("server_person_id", type=int, help="Server Person Id")
    args = parser.parse_args()

    main(args.sqlite_file, str(args.server_person_id))
