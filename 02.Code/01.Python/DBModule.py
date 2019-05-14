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
			
			sql = 'INSERT INTO ' + tableName.strip()

                        if tableNmae in ['S_JSON', 'T_JSON']:
                                sql += 'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);'
                                curs.execute(sql, values[0][26:30] + '01' if values[0][4:7] == 'Jan' else
                                                                     '02' if values[0][4:7] == 'Feb' else
                                                                     '03' if values[0][4:7] == 'Mar' else
                                                                     '04' if values[0][4:7] == 'Apr' else
                                                                     '05' if values[0][4:7] == 'May' else
                                                                     '06' if values[0][4:7] == 'Jun' else
                                                                     '07' if values[0][4:7] == 'Jul' else
                                                                     '08' if values[0][4:7] == 'Aug' else
                                                                     '09' if values[0][4:7] == 'Sep' else
                                                                     '10' if values[0][4:7] == 'Oct' else
                                                                     '11' if values[0][4:7] == 'Nov' else '12'
                                                                   + values[0][8:10]
                                                                   + values[0][11:19]
                                             , values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8])
                        elif tableNmae in ['S_HASHTAG', 'T_JHASHTAG']:
                                sql += 'VALUES(%s, %s, %s, %s);'
                                curs.execute(sql, values[0], values[1], values[2], values[3])
                        elif tableNmae in ['S_USER', 'T_USER']:
                                sql += 'VALUES(%s, %s, %s, %s, %s, %s);'
                                curs.execute(sql, values[0], values[1], values[2], values[3], values[4], values[5])
                        conn.commit()
			'''
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
			'''
	
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
			if database == 'search':
				# delete all data in the table
				sql = "delete from S_HASHTAG;"              
				curs.execute(sql)
				sql = "delete from S_USER;"
				curs.execute(sql)
				sql = "delete from S_JSON;"
				curs.execute(sql)
				conn.commit()
			elif database == 'timeline':
				# delete all data in the table
				sql = "delete from T_HASHTAG;"              
				curs.execute(sql)
				sql = "delete from T_USER;"
				curs.execute(sql)
				sql = "delete from T_JSON;"
				curs.execute(sql)
				conn.commit()
			elif database == 'keyword_count':
				sql = "delete from KEYWORD_COUNT;"
				curs.execute(sql)
				conn.commit()
			elif database == 'hashtag_count':
				sql = "delete from HASHTAG_COUNT;"
				curs.execute(sql)
				conn.commit()
		except :
			print("Delete Failed")		 
		finally :
			# MariaDB Connection and Cursor Close
			self.dbClose(conn,curs)





	

