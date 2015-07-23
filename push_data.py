#!/usr/bin/python

import dbs

serverPersonId = "1"

def main():
    (db_mysql, cur_mysql) = dbs.connect_mysql()
    (db_sqlite, cur_sqlite) = dbs.connect_sqlite()

    sqlite_tables = dbs.get_name_of_tables(cur_sqlite)

    for table in sqlite_tables:
        results = cur_sqlite.execute("SELECT * FROM " + table)

        for row in results.fetchall():
            insert = "INSERT INTO " + table + " VALUES( " + serverPersonId + ", "
            str_row = []
            for r in row:
                r = str(r).replace("'", '')
                str_row.append("'" + r + "'")
                #str_row.append("'" + str(r).replace("'", "\\'") + "'")

            insert += ",".join(str_row)

            insert += ")"

            print insert
            cur_mysql.execute(insert)

    db_mysql.commit()

if __name__ == '__main__':
    main()
