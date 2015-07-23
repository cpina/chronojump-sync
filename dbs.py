import MySQLdb
import sqlite3
import re

def connect_sqlite(file_name = None):
    if file_name is None:
        file_name = "Chronojump/database/chronojump.db"

    conn = sqlite3.connect(file_name)

    return (conn, conn.cursor())

def connect_mysql():
    conn = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='tissues',
        db='chronojump'
        )

    return (conn, conn.cursor())

def get_name_of_tables_mysql(cur_mysql):
    return get_tables(cur_mysql, "select table_name from information_schema.tables where table_schema='chronojump'")

def get_name_of_tables_sqlite(cur_sqlite):
    return get_tables(cur_sqlite, "SELECT name FROM sqlite_master WHERE type='table'")

def get_tables(cur, query):
    cur.execute(query)

    tables = []

    for table in cur.fetchall():
        tables.append(table[0])

    return tables

def get_create_table(cur_sqlite, table_name):
    results = cur_sqlite.execute("select sql from sqlite_master where type = 'table' and name = '%s'" % table_name)
    return results.fetchall()[0][0]

def get_create_table_mysql(cur_mysql, table_name):
    sql = "show create table " + table_name
    cur_mysql.execute(sql)
    create_table = cur_mysql.fetchall()[0][1]

    create_table = create_table.replace('`serverPersonId` int(11) DEFAULT NULL,', '')

    create_table = re.sub("ENGINE=InnoDB.*", '', create_table)
    return create_table

def tuple_to_insert(table, values):
    insert = "INSERT INTO %s VALUES ( " % table

    cleaned_values = []

    first_value = True
    for value in values:
        if not first_value:
            cleaned_values.append("'" + str(value).replace("'", "\\'") + "'")

        first_value = False

    insert += ",".join(cleaned_values)

    insert += ")"

    return insert
