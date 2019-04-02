#
# DBModule.py
#     Title: (MariaDB , Python 의 연동 , 테이블조회를 Module화 한다.)
#    Author: Bae In Gyu
# Create_at: 2019-04-02
# 
#

import pymysql

class DBClass :
	def select (table) :
		# 접속
		conn = pymysql.connect(host = 'localhost', user = 'root', password = '1234', db = 'mysql', charset = 'utf8')
		
		# Cursor 생성
		curs = conn.cursor()

		# 테이블 조회
		select = "select * from "+table
		curs.execute(select)
		
		# 테이블 데이터출력
		rows = curs.fetchall()
		for data in rows:
			print(list(data)) 

		# Connection 닫기
		conn.close()
