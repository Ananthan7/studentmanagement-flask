import sqlite3

con = sqlite3.connect('studentlist.db')
print('opened db successfully')
con.execute("CREATE TABLE student(Name TEXT, Address TEXT, City TEXT, Pin TEXT)")
print("Table created successfully")
con.close()