import sqlite3

def insertVaribleIntoTable(id, name, deptid, mobileno, salary):
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO emp
                          (empno,empname,deptid,mobileno,salary) 
                           VALUES 
                          (?,?,?,?,?)"""

        data_tuple = (id, name, deptid, mobileno, salary)
        cursor.execute(sqlite_insert_query, data_tuple)
        #print(cursor.rowcount)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

insertVaribleIntoTable(132, 'Joe', 3,4,5)
#insertVaribleIntoTable(13, 'Ben', 6,7,8)