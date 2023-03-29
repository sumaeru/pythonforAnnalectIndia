import sqlite3

def getDeveloperInfo(id):
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from emp where empno = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
            print("empno  = ", row[0])
            print("empname  = ", row[1])
            print("deptid  = ", row[2])
            print("mobileno  = ", row[3])
            print("salary  = ", row[4])
            
        else:
            print("no empno found")
            
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

getDeveloperInfo(10)