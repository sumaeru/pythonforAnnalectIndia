import sqlite3

def updateSqliteTable(id, salary):
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update emp set salary = ? where empno = ?"""
        data = (salary, id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        if cursor.rowcount != 0:
            print("update successful")
        else:
            print("no rows where found in the table matching the where condition")


        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")

updateSqliteTable(133, 7500)