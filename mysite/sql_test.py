import sqlite3  
conn = sqlite3.connect("db.sqlite3") 
print 'Opened database successfully'   
sql = "select url from Record_urls where id = 2"  
result = conn.execute(sql)
for i in result:
	if 'image' in i[0]:
		print i[0]
url = 'asdasdJPG'
if 'jpg' in url.lower() :
	print "yes"