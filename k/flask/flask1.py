import sqlite
con=sqlite3=connect('database.db')
print('opened database successfull')
conn.execute('CREATE TABLE student(name TEXT,addr TEXT,city TEXT,pin TEXT'))
print("Table created successfully")
con.close
