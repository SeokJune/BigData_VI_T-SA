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
			if bool(result[0] or result[1] or result[2] or result[3] or result[4] or result[5]) == True :
				return True
			
		except :
			print("파악실패")
		
		finally :
			# Select후 Cursor종료 및 MariaDB연결종료                
			self.dbClose()

	# 테이블의 데이터 모두조회함수----------------------------------------------------------------
	def selectDB(self,tableName) :
		try :
			# MariaDB연결 및 Cursor생성
			conn, curs = self.dbConnect()
			# 테이블 조회
			sql = "select * from "+tableName.strip()+";"
			curs.execute(sql)

			# 테이블 데이터출력	
			result = curs.fetchall()

			return result

		except :
			print("조회실패")
		
		finally :
			# Select후 Cursor종료 및 MariaDB연결종료                
			self.dbClose()

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

	# 테이블의 데이터 삽입함수--------------------------------------------------------------------
	def insertDB (self, tableName, values) :
		try :
			# MariaDB연결 및 Cursor생성
			conn, curs = self.dbConnect()
			
			# Data삽입

			if tableName == 'KEYWORD_JSON':
				sql = "insert into " + tableName.strip() + " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
				curs.execute(sql,(values[0],values[2],values[3],values[4],values[5],
						  values[6],values[11],values[19],values[20],values[23]))
				conn.commit()
				print("삽입완료")

			elif tableName == 'KEYWORD_HASHTAG':			
				sql = "insert into " + tableName.strip() + " values("
				sql += "'" + str(values[0]) + "',"
				sql +=       str(values[2][0]) + "," 
				sql +=       str(values[2][1]) + ","
				sql += "'" + str(values[1]) + "');"
				curs.execute(sql)
				conn.commit()
				print("삽입완료")


			#else if tableName == 'KEYWORD_METADATA':			
			#	sql = "insert into " + tableName.strip() + " values("

			#else if tableName == 'KEYWORD_USER':			
			#	sql = "insert into " + tableName.strip() + " values("

			#else if tableName == 'KEYWORD':			
			#	sql = "insert into " + tableName.strip() + " values("

			#else if tableName == 'HASHTAG':			
			#	sql = "insert into " + tableName.strip() + " values("
			



		except :
			print("삽입실패")

		finally :
			#Cursor종료 및 MariaDB연결종료
			self.dbClose()

	# Keyword Date Count 함수--------------------------------------------------------------------
	def keywordDateCount (self, tableName):
		try : 
			# MariaDB연결 및 Cursor생성
			conn, curs = self.dbConnect()

			# Keyword Date Count(Date 수정하고 sql문 수정해야함)
			sql = "select HCODE, COUNT(*) from " + tableName.strip() + " group by HCODE;"              
			curs.execute(sql)
			
			result = curs.fetchall()

			return result
			print("Date Count 조회")

		except :
			print("Date Count 조회실패")		 

		finally :
			# Cursor종료 및 MariaDB연결종료 
			self.dbClose()
