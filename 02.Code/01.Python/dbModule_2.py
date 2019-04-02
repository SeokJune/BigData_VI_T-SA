'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 
 dbModule.py
     Title: (MariaDB연결,종료 및 DML 작업)
    Author: Bae In Gyu
 Create_at: 2019-04-02
  Alter_at: 2019-04-03
      paln: insert(해당 테이블의 코드 존재 여부 파악) , connect(예외처리) 등

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import pymysql



class dbModule :
	host = 'localhost'  # 접속할 mysql server 주소
	user = 'root'       # 접속할 mysql ID
	pswd = '1234'       # 접속할 mysql ID의 암호
	db = 'mysql'        # 접속할 데이터베이스
	charset = 'utf8'    # mysql에서 select할때 한글이 깨질 수 있으므로 설정


	#MariaDB연결 함수
	def dbconn() :
		return pymysql.connect(host = dbModule.host, 
      	                               user = dbModule.user, 
				       password = dbModule.pswd, 
		                       db = dbModule.db, 
		                       charset = dbModule.charset)

	#MariaDB연결종료 함수
	#def dbclose() :
	#	return dbModule.dbconn().close()
				

	#Select 함수
	def select (table) :
		# MariaDB연결 및 Cursor 생성
		conn = dbModule.dbconn()
		curs = conn.cursor()
		
		# 테이블 조회
		select = "select * from "+table;
		curs.execute(select)
		
		# 테이블 데이터출력
		rows = curs.fetchall()
		for data in rows :
			print(data)
                
		# Select종료시 MariaDB연결종료
		conn.close()


	#Delete	
	def delete (table) :
		# MariaDB연결 및 Cursor 생성
		conn = dbModule.dbconn()
		curs = conn.cursor()

		# Data삭제
		delete = "delete from "+table
		curs.execute(delete)
		conn.commit()

		# Connection 닫기
		conn.close()

