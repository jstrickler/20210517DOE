#!/usr/bin/env python
import ibm_db_dbi as db

conn = db.connect("DATABASE=testdb;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=scripts;", "", "")

cursor = conn.cursor()

# select first name, last name from all presidents
if cursor.execute('''
    select lastname, firstname
    from presidents
'''):

    for row in cursor.fetchall():
        print(row)

# cursor.fetchone() and cursor.fetchmany() are also available
