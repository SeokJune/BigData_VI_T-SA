'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 dbModule.py
     Title: MariaDB연결,종료 및 DML 작업
    Author: Bae InGyu
 Create_at: 2019.04.02.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



import pymysql






class dbModule :
	


	'''
	 Modifier: Bae InGyu
	Modify on: 2019.04.05.
	연결상태 예외처리 추가 
	'''
	# 클래스의 생성자----------------------------------------------------------------------------	
	def __init__(self,host,user,pswd,db,charset) :   
		self.host = host
		self.user = user
		self.pswd = pswd       
		self.db = db        
		self.charset = charset


	# MariaDB연결함수----------------------------------------------------------------------------
	def dbConnect(self) :
		global conn
		conn = pymysql.connect(host = self.host, user = self.user, password = self.pswd, db = self.db, charset = self.charset)
			
		if conn.open == True :              
			print("========DB연결성공========")
		else :
			print("========DB연결실패========")




	'''
 	 Modifier: Bae InGyu
	Modify on: 2019.04.03. 
	MariaDB연결기능 함수선언	
	
	class dbModule :
	host = 'localhost'  # 접속할 mysql server 주소
	user = 'root'       # 접속할 mysql ID
	pswd = '1234'       # 접속할 mysql ID의 암호
	db = 'mysql'        # 접속할 데이터베이스
	charset = 'utf8'    # mysql에서 select할때 한글이 깨질 수 있으므로 설정

	# MariaDB연결함수
	def dbconn() :
		return pymysql.connect(host = dbModule.host, user = dbModule.user, password = dbModule.pswd, db = dbModule.db, charset = dbModule.charset)
                
	'''  
                                     
	'''
	Modifier: Bae InGyu
	Modify on: 2019-04-04.
	__init__함수추가
 	

	def __init__(self,host,user,pswd,db,charset):
		self.host = host         
		self.user = user
		self.pswd = pswd       
		self.db = db        
		self.charset = charset

	# MariaDB연결함수
	def dbconn(self):
		global conn 
		conn = pymysql.connect(host = self.host, user = self.user, password = self.pswd, db = self.db, charset = self.charset)
		print("DB연결 완료")
	'''
	#===========================================================================================#



	'''
	 Modifier: Bae InGyu
	Modify on: 2019.04.05.
	연결상태 예외처리 추가 
	'''
	# MariaDB연결종료함수-------------------------------------------------------------------------
	def dbClose(self) :
		conn.close()

		if conn.open == True :                            
			print("========DB연결성공========")
		else :
			print("========DB연결종료========")


	'''
	 Modifier: Bae In Gyu
	Modify on: 2019.04.04.
	MariaDB연결종료함수추가	

	# MariaDB연결종료함수
	def dbclose(self) :
                conn.close()
                print("DB연결 종료")
	'''
	#===========================================================================================#



	'''
	 Modifier: Bae InGyu
	Modify on: 2019.04.05.
	테이블의 Row 존재여부 파악 함수추가 
	'''

	# 해당 테이블에 레코드 존재파악 함수------------------------------------------------------------ 
	def getRowByCheck(self,table) :
                    
		# 데이터가 없으면 false 있으면 True
		if bool(self.selectDB(table)) == True :
			return True 
                     
		else : 
			return False

	#===========================================================================================#
	


	'''
	 Modifier: Bae InGyu
	Modify on: 2019-04-06 
	try ~ fianlly 추가
	'''
         
	# 테이블의 데이터 모두조회함수----------------------------------------------------------------
	def selectDB(self,table) :
		try :
			# MariaDB연결 및 Cursor생성
			self.dbConnect()
			curs = conn.cursor()

			# 테이블 조회
			sql = "select * from "+table.strip()+";"
			curs.execute(sql)

			# 테이블 데이터출력	
			rows = curs.fetchall()
			result = rows

			return result

		except :
			print("조회실패")
		
		finally :
			# Select후 Cursor종료 및 MariaDB연결종료
			curs.close()                 
			self.dbClose()
                 		
                    

	'''
	 Modifier: Bae InGyu
	Modify on: 2019-04-03
	select기능 함수선언
 
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

	'''

	'''
	 Modifier: Bae In Gyu
	Modify on: 2019-04-04 Code
	결과값 return result로 변경

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

	'''
	 Modifier: Bae In Gyu
	Modify on: 2019-04-05 Code
	Cursor()종료추가 , 테이블명 입력시 양쪽끝 공백있을시 제거기능 추가
	
	# 테이블의 데이터 모두조회함수
	def selectDB(self,table) :
		  # MariaDB연결 및 Cursor생성
                  self.dbConnect()
                  curs = conn.cursor()

		  # 테이블 조회
                  sql = "select * from "+table.strip()+";"
                  curs.execute(sql)

		  # 테이블 데이터출력	
                  rows = curs.fetchall()

                  result = rows
		
		  # Select후 Cursor종료 및 MariaDB연결종료
                  curs.close()                 
                  self.dbClose()
                 		
                  return result

	'''
	#===========================================================================================#



	'''
	Modifier: Bae In Gyu
	Modify on: 2019-04-06 
	try ~ fianlly 추가
	'''

	# 테이블의 데이터 모두삭제함수----------------------------------------------------------------	
	def deleteDB (self,table) :
		try : 
			# MariaDB연결 및 Cursor생성
			self.dbConnect()
			curs = conn.cursor()

			# Data삭제
			sql = "delete from "+table.strip()+";"              
			curs.execute(sql)
			conn.commit()
			print("삭제완료")

		except :
			print("삭제실패")		 

		finally :
			# Connection 닫기
			curs.close() 
			self.dbClose()
                 

	'''
 	Modifier: Bae In Gyu
	Modify on: 2019-04-03 Code
	delete기능 함수선언

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

	'''
	 Modifier: Bae In Gyu
	Modify on: 2019-04-05 Code
	Cursor()종료추가 , 테이블명 입력시 양쪽끝 공백있을시 제거기능 추가

	# 테이블의 데이터 모두삭제함수(예외처리추가예정)	
	def deleteDB (self,table) :
		# MariaDB연결 및 Cursor생성
                self.dbConnect()
                curs = conn.cursor()

		# Data삭제
                sql = "delete from "+table.strip()+";"              
                curs.execute(sql)
                conn.commit()

		# Connection 닫기
                curs.close() 
                self.dbClose()

                print("삭제완료")

	# insert 함수 추가 예정
	#def insertDB (table) :

	'''
	#===========================================================================================#



	'''
	Modifier: Bae In Gyu
	Modify on: 2019-04-06 
	insertDB 함수추가
	'''

	# 테이블의 데이터 삽입함수--------------------------------------------------------------------
	def insertDB (self,table,values) :
		try :
			# MariaDB연결 및 Cursor생성
			self.dbConnect()
			curs = conn.cursor()
			self.values = values 
			sql = "insert into "+table.strip()+values
			curs.execute(sql)
			conn.commit()
			print("삽입완료")

		except :
			print("삽입실패")

		finally :
			# Connection 닫기
			curs.close() 
			self.dbClose()





















    







	
