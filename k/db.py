import sqlite3
con=sqlite3.connect('database3.db')
print('opened database successfull')
con.execute('CREATE TABLE student(Name TEXT,Address TEXT,City TEXT,Pin TEXT);')
print("Table created successfully")
con.close()
