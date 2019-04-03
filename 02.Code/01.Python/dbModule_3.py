'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

 dbModule_3.py
     Title: (MariaDB연결,종료 및 DML 작업)
    Author: Bae In Gyu
 Create_at: 2019-04-02
 
      
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import pymysql


class dbModule_3 :

	
	'''
	 Modifier: Bae In Gyu 
 	Modify on: 2019-04-04
 	클래스 생성자 추가(MariaDB와 연결시 기존에는 파라미터를 dbModule_3.py에서 수정해야했던걸 dbMain_3.py에서 수정하게변경)
	'''

	# 클래스의 생성자
	def __init__(self,host,user,pswd,db,charset):
					self.host = host         
					self.user = user
					self.pswd = pswd       
					self.db = db        
					self.charset = charset

	# MariaDB연결 
	def dbconn(self):
                global conn 
                conn = pymysql.connect(host = self.host, user = self.user, password = self.pswd, db = self.db, charset = self.charset)
                print("DB연결 완료")

       
	'''
	 Modifier: Bae In Gyu
	Modify on: 2019-04-04
	MariaDB연결종료 함수 추가 
	'''

	# MariaDB연결종료
	def dbclose(self) :
                conn.close()
                print("DB연결 종료")			



	# 해당 테이블에 코드 존재파악 추가 계획
	#def getCodeByCheck() :


	'''
	 Modifier: Bae In Gyu
	Modify on: 2019-04-04
	조회한 데이터를 return하여 dbMain_3.py에서 출력되게 변경
	MariaDB와 연결시 dbMain_3.py에서 수정하게 변경하면서 생긴 에러 해결
	'''	

	# 테이블의 데이터 모두조회
	def selectDB (self,table) :
		# MariaDB연결 및 Cursor생성
                dbModule_3.dbconn(self)
                curs = conn.cursor()

		# 테이블 조회
                sql = "select * from "+table+";"
                curs.execute(sql)


		# 테이블 데이터출력	
                rows = curs.fetchall()
                result = rows
		
		# Select종료시 MariaDB연결종료
                dbModule_3.dbclose(self)
		
                print("조회완료")
                return result


	'''
	 Modifier: Bae In Gyu
	Modify on: 2019-04-04
	MariaDB와 연결시 dbMain_3.py에서 수정하게 변경하면서 생긴 에러 해결
	'''	

	# 테이블의 데이터 모두삭제	
	def deleteDB (self,table) :
		# MariaDB연결 및 Cursor생성
                dbModule_3.dbconn(self)
                curs = conn.cursor()

		# Data삭제
                sql = "delete from "+table+";"              
                curs.execute(sql)
                conn.commit()

		# Connection 닫기
                dbModule_3.dbclose(self)

                return print("삭제완료")

	# insert 함수 추가 계획
	#def insertDB (table) :




'''
수정전 코드

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
'''


