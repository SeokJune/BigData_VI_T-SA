# DBModule.py
#     Title: MariaDB connection and close, SQL command DML(Data Manipulation Language) processing
#    Author: Bae InGyu
#--------------------------------------------------------------------------------------------------
#Modules for Python to MariaDB Interworking
import pymysql
# -------------------------------------------------------------------------------------------------
#  Class Name: DBModule:
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
		# Generating Dictionary Cursor		
		curs = conn.cursor()
		# 'conn', 'curs' return
		return conn , curs 
	# -----------------------------------------------------------------------------------------
	# dbClose
	# -----------------------------------------------------------------------------------------
	def dbClose(self,conn,curs) :
		conn , curs = self.dbConnect()
                # MariaDB Connection and Cursor Close
		# 'conn.close()', 'curs.close()' return
		return conn.close() , curs.close()
	# -----------------------------------------------------------------------------------------
	# selectDB
	# -----------------------------------------------------------------------------------------
	def dbSelect(self, cols, tabs, cond) :
		try :
			# MariaDB Connection and Generating Dictionary Cursor
			conn, curs = self.dbConnect()
			# select all data in the table
			sql = "select %s from %s %s;" %(cols, tabs, cond)
			curs.execute(sql)
			# fetchall data	
			result = curs.fetchall()
			# 'result' return
			return result
		except :
			print("Select Failed")
		finally :
			# MariaDB Connection and Cursor Close              
			self.dbClose(conn,curs)
	# -----------------------------------------------------------------------------------------
	# insertDB
	# -----------------------------------------------------------------------------------------
	def dbInsert(self, tableName, values) :
		try :
			# MariaDB Connection and Generating Dictionary Cursor
			conn, curs = self.dbConnect()
			# insert data in the table
			if tableName == 'S_HASHTAG':
				sql = "insert into " + tableName.strip() + " values(%s,%s,%s,%s);"
				curs.execute(sql,(values[0],values[1],values[2],values[3]))
				conn.commit()
				print("Insert Complete") 	

			elif tableName == 'S_USER':
				sql = "insert into " + tableName.strip() + " values(%s,%s,%s,%s,%s,%s);"
				curs.execute(sql,(values[0],values[1],values[2],values[3],values[4],values[5]))
				conn.commit()
				print("Insert Complete")

			elif tableName == 'S_JSON':
				values[0] = values[0].replace('Apr','04')
				values[0] = '-'.join([values[0][25:],values[0][4:6],values[0][7:19]])
				sql = "insert into " + tableName.strip() + " values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
				curs.execute(sql,(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8]))
				conn.commit()
				print("Insert Complete")

			if tableName == 'T_HASHTAG':
				sql = "insert into " + tableName.strip() + " values(%s,%s,%s,%s);"
				curs.execute(sql,(values[0],values[1],values[2],values[3]))
				conn.commit()
				print("Insert Complete") 	

			elif tableName == 'T_USER':
				sql = "insert into " + tableName.strip() + " values(%s,%s,%s,%s,%s,%s);"
				curs.execute(sql,(values[0],values[1],values[2],values[3],values[4],values[5]))
				conn.commit()
				print("Insert Complete")

			elif tableName == 'T_JSON':
				values[0] = values[0].replace('Apr','04')
				values[0] = '-'.join([values[0][25:],values[0][4:6],values[0][7:19]])
				sql = "insert into " + tableName.strip() + " values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
				curs.execute(sql,(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8]))
				conn.commit()
				print("Insert Complete")	
	
		except:
			print("Insert Failed")

		finally:
			# MariaDB Connection and Cursor Close
			self.dbClose(conn,curs)

	# -----------------------------------------------------------------------------------------
	# deleteDB 수정하기 search , timeline , keyword count , hashtag count
	# -----------------------------------------------------------------------------------------
	def dbDelete(self,database) :
		try : 
			# MariaDB Connection and Generating Dictionary Cursor
			conn, curs = self.dbConnect()
			# delete all data in the table
			sql = "delete from "+table.strip()+";"              
			curs.execute(sql)
			conn.commit()
		except :
			print("Delete Failed")		 
		finally :
			# MariaDB Connection and Cursor Close
			self.dbClose(conn,curs)
	# -----------------------------------------------------------------------------------------
	# keywordDateCount
	# -----------------------------------------------------------------------------------------
	def keywordDateCount (self, tableName):
		try : 
			# MariaDB Connection and Generating Dictionary Cursor
			conn, curs = self.dbConnect()
			# Keyword Date Count
			sql = "select date_format(create_at,'%Y-%m-%d') create_at, count(*) from " + tableName.strip() + " group by date_format(create_at, '%Y-%m-%d');"              
			curs.execute(sql)
			result = curs.fetchall()
			return result
		except :
			print("Created_at Count Select failed")		 
		finally :
			# Cursor종료 및 MariaDB연결종료 
			self.dbClose(conn,curs)






	

