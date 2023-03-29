import sqlite3

conn = sqlite3.connect('test.db')
conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL)''')
    

print("Opened database successfully")

