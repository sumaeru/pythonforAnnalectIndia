import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE) \
      VALUES (3, 'def', 55 )");
print("inserted successfully")

conn.commit()
conn.close()