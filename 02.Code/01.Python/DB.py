/*
* Author : Bae In Gyu
* Create_at : 2019-04-02 
*/

import pymysql
 
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='chosun',
                       db='mysql', charset='utf8')


# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 
# SQL문 실행
sql = "select * from Student"
curs.execute(sql)
 
# 데이타 Fetch
rows = curs.fetchall()
for data in rows:
	print(data)    
 
# Connection 닫기
conn.close()


