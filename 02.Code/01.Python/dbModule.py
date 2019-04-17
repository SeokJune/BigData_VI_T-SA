'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 dbModule.py
     Title: MariaDB연결,종료 및 DML 작업
    Author: Bae InGyu
 Create_at: 2019.04.02.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



import pymysql






class dbModule :
	
	# 클래스의 생성자----------------------------------------------------------------------------	
	def __init__(self,host,user,pswd,db,charset) :   
		self.host = host
		self.user = user
		self.pswd = pswd       
		self.db = db        
		self.charset = charset


	# MariaDB연결함수----------------------------------------------------------------------------
	def dbConnect(self) :
		conn = pymysql.connect(host = self.host, user = self.user, password = self.pswd, db = self.db, charset = self.charset)
		curs = conn.cursor()
		return conn , curs 




	# MariaDB연결종료함수-------------------------------------------------------------------------
	def dbClose(self) :
		conn , curs = self.dbConnect()
		return conn.close() , curs.close()


	'''
 	 Modifier: Bae InGyu
	Modify on: 2019-04-17 
	기존의 하나의 테이블만 ROW 여부파악에서 모든 테이블의 ROW 여부파악으로 수정
	'''

	# 모든테이블에 ROW 여부파악 함수------------------------------------------------------------ 
	def getRowByCheck(self,tableName) :
		try :	
			# MariaDB연결 및 Cursor생성
			conn, curs = self.dbConnect()

			# 테이블 조회
			result = []
			i = 0
			for table in tableName :
				sql = "select * from "+table.strip()+";"
				curs.execute(sql)
        
				# 테이블 데이터출력
				result.append(curs.fetchall())		
				print(result[i])
				i += 1
				
			# 모든 테이블 ROW 여부파악 하나의 테이블이라도 ROW가 존재하면 True로 반환
			if bool(result[0] or result[1] or result[2] or result[3] or result[4]) == True :
				return True
			
		except :
			print("파악실패")
		
		finally :
			# Select후 Cursor종료 및 MariaDB연결종료                
			self.dbClose()



	'''
	def getRowByCheck(self,table) :
               	# 데이터가 없으면 false 있으면 True
		if bool(self.selectDB(table)) == True :
			return True 
		else : 
			return False
	'''


         
	# 테이블의 데이터 모두조회함수----------------------------------------------------------------
	def selectDB(self,table) :
		try :
			# MariaDB연결 및 Cursor생성
			conn, curs = self.dbConnect()
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
			self.dbClose()
                 		
                    
	'''
 	 Modifier: Bae InGyu
	Modify on: 2019-04-17 
	기존의 하나의 테이블의 ROW만 삭제에서 모든 테이블의 ROW 삭제로 변경
	'''


	# 모든테이블의 데이터 모두삭제함수----------------------------------------------------------------	
	def deleteDB (self,tableName) :
		try : 
			# MariaDB연결 및 Cursor생성
			conn, curs = self.dbConnect()

			# Data삭제
			for table in tableName :
				sql = "delete from "+table.strip()+";"              
				curs.execute(sql)
				conn.commit()
				print("삭제완료")

		except :
			print("삭제실패")		 

		finally :
			# Cursor종료 및 MariaDB연결종료 
			self.dbClose()
                 


	'''
	def deleteDB (self,table) :
		try : 
			# MariaDB연결 및 Cursor생성
			conn, curs = self.dbConnect()

			# Data삭제
			sql = "delete from "+table.strip()+";"              
			curs.execute(sql)
			conn.commit()
			print("삭제완료")

		except :
			print("삭제실패")		 

		finally :
			# Cursor종료 및 MariaDB연결종료 
			self.dbClose()
	'''



	# 테이블의 데이터 삽입함수--------------------------------------------------------------------
	def insertDB (self,test,values) :
		try :
			# MariaDB연결 및 Cursor생성
			conn, curs = self.dbConnect()

			# Data삽입
			self.values = values			
			sql = "insert into "+table.strip()+"values"+values+";"
			curs.execute(sql)
			conn.commit()
			print("삽입완료")

		except :
			print("삽입실패")

		finally :
			# Cursor종료 및 MariaDB연결종료
			self.dbClose()


