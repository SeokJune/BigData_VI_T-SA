# DBModule.py
#     Title: MariaDB connection and close, SQL command DML(Data Manipulation Language) processing
#    Author: Bae InGyu
# Create_at: 2019.04.02
#--------------------------------------------------------------------------------------------------
import pymysql #Modules for Python to MariaDB Interworking
# -------------------------------------------------------------------------------------------------
#  Class Name: dbModule:
# Method list: dbConnect, dbClose
#            : selectDB, insertDB, deleteDB
#            : keywordDateCount
# -------------------------------------------------------------------------------------------------
class DBModule :
	# -----------------------------------------------------------------------------------------
	# Generator
	# Set: host, user, pswd, db, charset
	# -----------------------------------------------------------------------------------------
	def __init__(self,host,user,pswd,db,charset) :   
		self.host = host
		self.user = user
		self.pswd = pswd       
		self.db = db        
		self.charset = charset
	# -----------------------------------------------------------------------------------------
	# dbConnect
	# -----------------------------------------------------------------------------------------
	def dbConnect(self) :
		# MariaDB Connection
		conn = pymysql.connect(host = self.host, user = self.user, password = self.pswd, db = self.db, charset = self.charset)
		# Generating Dictoionary Cursor		
		curs = conn.cursor()
		# 'conn', 'curs' return
		return conn , curs 
	# -----------------------------------------------------------------------------------------
	# dbClose
	# -----------------------------------------------------------------------------------------
	def dbClose(self) :
		conn , curs = self.dbConnect()
                # MariaDB Connection and Cursor Close
		# 'conn.close()', 'curs.close()' return
		return conn.close() , curs.close()
	# -----------------------------------------------------------------------------------------
	# selectDB
	# -----------------------------------------------------------------------------------------
	def selectDB(self,tableName) :
		try :
			# MariaDB Connection and Generating Dictoionary Cursor
			conn, curs = self.dbConnect()
			# select all data in the table
			sql = "select * from "+tableName.strip()+";"
			curs.execute(sql)
			# fetchall data	
			result = curs.fetchall()
			# 'result' return
			return result
		except :
			print("Select Failed")
		finally :
			# MariaDB Connection and Cursor Close              
			self.dbClose()
	# -----------------------------------------------------------------------------------------
	# insertDB
	# -----------------------------------------------------------------------------------------
	def insertDB (self, tableName, values) :
		try :
			# MariaDB Connection and Generating Dictoionary Cursor
			conn, curs = self.dbConnect()
			# insert data in the table
			if tableName == 'KEYWORD_JSON':                                
				values[0] = '-'.join([values[0][26:],values[0][4:7],values[0][8:19]])
				values[0] = values[0].replace('May','05')
				sql = "insert into " + tableName.strip() + " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
				curs.execute(sql,(values[0],values[2],values[3],values[4],values[5],
						  values[6],values[11],values[19],values[20],values[23]))
				conn.commit()
				print("Insert Complete")

			elif tableName == 'KEYWORD_HASHTAG':			
				sql = "insert into " + tableName.strip() + " values("
				sql += "'" + str(values[0]) + "',"
				sql +=       str(values[2][0]) + "," 
				sql +=       str(values[2][1]) + ","
				sql += "'" + str(values[1]) + "');"
				curs.execute(sql)
				conn.commit()
				print("Insert Complete")

			#else if tableName == 'KEYWORD_METADATA':			
			#	sql = "insert into " + tableName.strip() + " values("

			#else if tableName == 'KEYWORD_USER':			
			#	sql = "insert into " + tableName.strip() + " values("

			#else if tableName == 'KEYWORD':			
			#	sql = "insert into " + tableName.strip() + " values("

			#else if tableName == 'HASHTAG':			
			#	sql = "insert into " + tableName.strip() + " values("
			

		except :
			print("Insert Failed")

		finally :
			# MariaDB Connection and Cursor Close
			self.dbClose()

	# -----------------------------------------------------------------------------------------
	# deleteDB
	# -----------------------------------------------------------------------------------------
	def deleteDB (self,tableName) :
		try : 
			# MariaDB Connection and Generating Dictoionary Cursor
			conn, curs = self.dbConnect()
			# delete all data in the table
			sql = "delete from "+table.strip()+";"              
			curs.execute(sql)
			conn.commit()
		except :
			print("Delete Failed")		 
		finally :
			# MariaDB Connection and Cursor Close
			self.dbClose()
	# -----------------------------------------------------------------------------------------
	# keywordDateCount
	# -----------------------------------------------------------------------------------------
	def keywordDateCount (self, tableName):
		try : 
			# MariaDB Connection and Generating Dictoionary Cursor
			conn, curs = self.dbConnect()
			# Keyword Date Count(Date 수정하고 sql문 수정해야함)
			sql = "select HCODE, COUNT(*) from " + tableName.strip() + " group by HCODE;"              
			curs.execute(sql)
			
			result = curs.fetchall()

			return result
		except :
			print("Created_at Count Select failed")		 
		finally :
			# Cursor종료 및 MariaDB연결종료 
			self.dbClose()




	

	'''
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

	'''


	

	

