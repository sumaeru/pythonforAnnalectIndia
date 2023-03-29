import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("UPDATE COMPANY set age = 44 where ID = 3")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
print("Total number of rows updated :", cursor.rowcount)



cursor = conn.execute("SELECT id, name, age from COMPANY")
for row in cursor:
   print("ID = ", row[0],
   "NAME = ", row[1],
    "age = ", row[2], "\n")

conn.close()