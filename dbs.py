import MySQLdb
import sqlite3

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

def get_name_of_tables(cur_sqlite):
    cur_sqlite.execute("SELECT name FROM sqlite_master WHERE type='table'")

    tables = []

    for table in cur_sqlite.fetchall():
        tables.append(table[0])

    return tables

def get_create_table(cur_sqlite, table_name):
    results = cur_sqlite.execute("select sql from sqlite_master where type = 'table' and name = '%s'" % table_name)
    return results.fetchall()[0][0]

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
