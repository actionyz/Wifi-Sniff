import sqlite3  
conn = sqlite3.connect("../db.sqlite3") 
print 'Opened database successfully'   
sql = "select * from Record_urls where id = 1"  
result = conn.execute(sql)
for i in result:
	print i[2]

