import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("delete from  COMPANY where ID = 3")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, age from COMPANY")
for row in cursor:
   print("ID = ", row[0],
   "NAME = ", row[1],
    "age = ", row[2], "\n")

conn.close()