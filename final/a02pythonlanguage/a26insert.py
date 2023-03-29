import sqlite3

try:
    sqliteConnection = sqlite3.connect('test.db')
    #above line will help you in contacting the database
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO emp
                          (empno,empname,deptid,mobileno,salary) 
                           VALUES 
                          (123,'a',2,3,4)"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")