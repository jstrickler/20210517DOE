#!/usr/bin/env python
import ibm_db_dbi as db

def dict_cursor(cursor):
    column_names = [c[0] for c in cursor.description]
    for row in cursor.fetchall():
        row_dict = dict(zip(column_names, row))
        yield row_dict

with db.connect("DATABASE=testdb;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=scripts;") as conn:

    cursor = conn.cursor()

    # select first name, last name from all presidents
    if cursor.execute('''
        select lastname, firstname
        from presidents
    '''):

        for row in cursor.fetchall():
            print(row)


    pres_data = [47, 'Jones', 'Mary', '1985-04-01', None, "Durham", "North Carolina",
                 '2025-01-20', None, 'Independent']

    sql_insert = """
    insert into presidents 
    (TERMNUM, LASTNAME, FIRSTNAME, BIRTHDATE, DEATHDATE, BIRTHPLACE, BIRTHSTATE, 
    TERMSTART, TERMEND, PARTY) 
    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    try:
        cursor.execute(sql_insert, pres_data)
        # multiple INSERT, UPDATE, etc
    except db.DatabaseError as err:
        print(err)
        conn.rollback()
    # cursor.executemany(sql_insert, LIST-OF-LISTS)
    else:
        pass
#        conn.commit()
    # conn.rollback()

    query = '''
        select lastname, firstname, party
        from presidents
    '''
    if cursor.execute(query):
        for row in dict_cursor(cursor):
            print(row['FIRSTNAME'], row['LASTNAME'], row['PARTY'])

    cursor.close()
    # cursor.fetchone() and cursor.fetchmany() are also available



"""
SQL_ATTR_AUTOCOMMIT = ibm_db.SQL_ATTR_AUTOCOMMIT
SQL_ATTR_CURRENT_SCHEMA = ibm_db.SQL_ATTR_CURRENT_SCHEMA
SQL_AUTOCOMMIT_OFF = ibm_db.SQL_AUTOCOMMIT_OFF
SQL_AUTOCOMMIT_ON = ibm_db.SQL_AUTOCOMMIT_ON
ATTR_CASE = ibm_db.ATTR_CASE
CASE_NATURAL = ibm_db.CASE_NATURAL
CASE_LOWER = ibm_db.CASE_LOWER
CASE_UPPER = ibm_db.CASE_UPPER
SQL_FALSE = ibm_db.SQL_FALSE
SQL_TRUE = ibm_db.SQL_TRUE
SQL_TABLE_STAT = ibm_db.SQL_TABLE_STAT
SQL_INDEX_CLUSTERED = ibm_db.SQL_INDEX_CLUSTERED
SQL_INDEX_OTHER = ibm_db.SQL_INDEX_OTHER
SQL_DBMS_VER = ibm_db.SQL_DBMS_VER
SQL_DBMS_NAME = ibm_db.SQL_DBMS_NAME
USE_WCHAR = ibm_db.USE_WCHAR
WCHAR_YES = ibm_db.WCHAR_YES
WCHAR_NO = ibm_db.WCHAR_NO
"""
