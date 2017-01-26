import sqlite3  
conn = sqlite3.connect("db.sqlite3") 
print 'Opened database successfully'   
sql = "select * from victim where mac = '14:2d:27:ba:151:47'"  
re = conn.execute(sql)
if re:
	print "a"
