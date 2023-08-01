""" import sqlite3 """

import pymysql

conn = pymysql.connect(

    host="localhost",
    database='my_database',
    user='my_user',
    password='my-secret-password',
    charset='utf8mb4'

)


""" conn = sqlite3.connect('books.sqlite') """

cursor = conn.cursor()
sql_query = """ CREATE TABLE book(
            id int AUTO_INCREMENT PRIMARY KEY,
            author text NOT NULL,
            language text NOT NULL,
            title text NOT NULL

)"""
cursor.execute(sql_query)
conn.close()