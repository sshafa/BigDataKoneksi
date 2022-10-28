import pymysql
db= pymysql.Connect(host= 'localhost' , user= 'root' , password= '', db= 'db_sma2')
cursor =db.cursor()
print(" Data Followers terbanyak")
cursor.execute("select*from tbl_scraping order by follower_count desc ")
data= cursor.fetchall()

for d in data:
	print(d)

print(" Data Followers tersedikit")         
cursor.execute("select*from tbl_scraping order by follower_count asc ")
dat= cursor.fetchall()

for dt in dat:
	print(dt) 