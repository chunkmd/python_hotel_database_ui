#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# https://www.sqlitetutorial.net/sqlite-python
# https://www.youtube.com/watch?v=RaESMr2DnGM -> Captain D.j Oamen
# 45:00, 52:08, 55:08, 1:00:18

# Craig Miles -> cmiles69@hushmail.com

import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, r'hotel.sqlite3')


def get_conn():
    con = None
    # db_file = ( r'employee.sqlite3' )
    try:
        con = sqlite3.connect(db_path,
                              detect_types=sqlite3.PARSE_COLNAMES | sqlite3.PARSE_DECLTYPES)
        # print( con )
        print(sqlite3.version)
        print('Successfull Connection!')
        return con
    except sqlite3.Error as e:
        print(e)


def insert_hotel_booking(booking):
    ''' Insert a new Hotel booking into the booking table '''
    conn = get_conn()

    sql_booking = ''' INSERT OR IGNORE INTO booking(
                                          Customer_ID,
                                          Firstname,
                                          Surname,
                                          Address,
                                          Birth_Date,
                                          Post_Code,
                                          Mobile,
                                          Email,
                                          Nationality,
                                          Gender,
                                          DateIn,
                                          DateOut,
                                          ID_Type,
                                          Meal_Type,
                                          Room_Type,
                                          Room_Number,
                                          Room_Phone )
                                          
                      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); '''
    db_cursor = conn.cursor()
    db_cursor.executemany(sql_booking, booking)
    conn.commit()
    db_cursor.execute('SELECT max( id ) FROM booking')
    max_id = db_cursor.fetchone()[0]
    db_cursor.close()
    conn.close()
    return (max_id)


def display_hotel_booking_record():
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    db_cursor.execute('''SELECT Customer_ID,
                                 Firstname,
                                 Surname,
                                 Mobile,
                                 Email
                           FROM booking''')
    table_data = db_cursor.fetchall()
    db_cursor.close()  # No conn.commit() needed here. Only viewing.
    conn.close()
    return table_data


def search_hotel_booking_record(record):
    sql_search = '''SELECT Customer_ID,
                           Firstname,
                           Surname,
                           Address,
                           Birth_Date,
                           Post_Code,
                           Mobile,
                           Email,
                           Nationality,
                           Gender,
                           DateIn,
                           DateOut,
                           ID_Type,
                           Meal_Type,
                           Room_Type,
                           Room_Number,
                           Room_Phone                  
                           FROM booking
                    WHERE  Customer_ID = ?'''

    conn = get_conn()
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    db_cursor.execute(sql_search, (record,))
    table_data = db_cursor.fetchone()
    db_cursor.close()
    conn.close()
    return (table_data)


def delete_hotel_booking_record(CID):
    conn = get_conn()
    db_cursor = conn.cursor()
    db_cursor.execute('''DELETE FROM booking
                          WHERE Customer_ID = ?''', (CID,))
    conn.commit()
    RC = db_cursor.rowcount
    db_cursor.close()
    conn.close()
    if RC > 1:
        return ('Successfully Deleted Database Record', RC)


def update_hotel_booking_record(booking):
    conn = get_conn()
    db_cursor = conn.cursor()

    try:
        db_cursor.executemany('''UPDATE booking SET
                                Customer_ID = ?,
                                Firstname   = ?,
                                Surname     = ?,
                                Address     = ?,
                                Birth_Date  = ?,
                                Post_Code   = ?,
                                Mobile      = ?,
                                Email       = ?,
                                Nationality = ?,
                                Gender      = ?,
                                DateIn      = ?,
                                DateOut     = ?,
                                ID_Type     = ?,
                                Meal_Type   = ?,
                                Room_Type   = ?,
                                Room_Number = ?,
                                Room_Phone  = ?
                              WHERE Customer_ID = ?;''', (booking))
        conn.commit()
        print('Record Updated Successfully')
    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (conn):
            db_cursor.close()
            conn.close()
            print("The SQLite connection is closed")


def create_table(conn, sql_script):
    ''' Create a database table from an sql statement'''

    try:
        db_cursor = conn.cursor()
        db_cursor.execute(sql_script)
        print('Create booking table success!')
    except sqlite3.Error as e:
        print(e)


def create_hotel_booking_table():
    ''' Create entire Hotel database including tables '''

    sql_create_hotel_booking_table = '''
                                CREATE TABLE IF NOT EXISTS booking(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Customer_ID TEXT NOT NULL,
                                Firstname   TEXT NOT NULL,
                                Surname     TEXT NOT NULL,
                                Address     TEXT NOT NULL,
                                Birth_Date  TEXT,
                                Post_Code   TEXT,
                                Mobile      TEXT,
                                Email       TEXT,
                                Nationality TEXT,
                                Gender      TEXT,
                                DateIn      TEXT,
                                DateOut     TEXT,
                                ID_Type     TEXT,
                                Meal_Type   TEXT,
                                Room_Type   TEXT,
                                Room_Number TEXT,
                                Room_Phone  TEXT ); '''

    # Create a database connection.
    conn = get_conn()

    # Create tables
    if conn is not None:
        # Create Hotel table
        create_table(conn, sql_create_hotel_booking_table)
        conn.commit()
        conn.close()
    else:
        print('Error!, Cannot create the database connection!')
        conn = None


def dumpSQL():
    conn = get_conn()
    with open('dump_hotel.sql', 'w', encoding='utf-8') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
    f.close()


if __name__ == '__main__':
    pass
    # create_hotel_booking_table()
