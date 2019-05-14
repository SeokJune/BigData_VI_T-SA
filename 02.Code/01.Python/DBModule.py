# DBModule.py
#  Title: MariaDB connection and close, SQL command DML(Data Manipulation Language) processing
# Author: Bae InGyu
# --------------------------------------------------------------------------------------------------
# Modules for Python to MariaDB Interworking
import pymysql
# --------------------------------------------------------------------------------------------------
#  Class Name: DBModule
# Method list: dbConnect, dbClose
#            : dbSelect, dbInsert, dbDelete
# -------------------------------------------------------------------------------------------------
class DBModule:
    # ----------------------------------------------------------------------------------------------
    # Generator
    # Set: host, user, pswd, dbNm, char
    # ----------------------------------------------------------------------------------------------
    def __init__(self, host, user, pswd, dbNm, char):
        self.host = host
        self.user = user
        self.pswd = pswd
        self.dbNm = dbNm
        self.char = char
    # ----------------------------------------------------------------------------------------------
    # Connect DataBase(MariaDB)
    # ----------------------------------------------------------------------------------------------
    def dbConnect(self):
        # Set up DB Connection Environment
        conn = pymysql.connect(host = self.host,     # IP
                               user = self.user,     # User ID
                               password = self.pswd, # User Password
                               db = self.dbNm,        # DB Name
                               charset = self.char)  # Encoding Character
        # Create Cursor
        curs = conn.cursor()
        # 'conn', 'curs' return
        return conn, curs
    # ----------------------------------------------------------------------------------------------
    # Close: Cursor, DataBase Connection
    # ----------------------------------------------------------------------------------------------
    def dbClose(self, curs, conn):
        curs.close()
        conn.close()
    # ----------------------------------------------------------------------------------------------
    # Load Data From Database
    # ----------------------------------------------------------------------------------------------
    def dbSelect(self, cols, tabs, cond):
        try:
            # DB Connect
            conn, curs = self.dbConnect()
            # Write Query: Select Data
            sql = 'SELECT %s FROM %s %s;' % (cols, tabs, cond)
            # Execute Query
            curs.execute(sql)
            # Fetch
            selectData = curs.fetchall()
            # 'selectData' return
            return selectData
        except:
            print('Error: Select Failed')
        finally:
            # DB Close
            self.dbClose(curs, conn)
    # ----------------------------------------------------------------------------------------------
    # Save Data to DataBase
    # ----------------------------------------------------------------------------------------------
    def dbInsert(self, tableNm, value):
        try:
            # DB Connect
            conn, curs = self.dbConnect()
            # Write Query: Select Data / Execute Query
            sql = 'INSERT INTO ' + tableNm
            if tableName in ['S_JSON', 'T_JSON']:
                sql += ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);'
                curs.execute(sql, (value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8]))
            elif tableName in ['S_HASHTAG', 'T_JHASHTAG']:
                sql += ' VALUES(%s, %s, %s, %s);'
                curs.execute(sql, (value[0], value[1], value[2], value[3]))
            elif tableName in ['S_USER', 'T_USER']:
                sql += ' VALUES(%s, %s, %s, %s, %s, %s);'
                curs.execute(sql, (value[0], value[1], value[2], value[3], value[4], value[5]))
            # Apply Query
            conn.commit()
        except:
            print('Error: Insert Failed')
        finally:
            # DB Close
            self.dbClose(curs, conn)
    # ----------------------------------------------------------------------------------------------
    # Elimination Data to DataBase
    # ----------------------------------------------------------------------------------------------
    def dbDelte(self, tableNm):
        try:
            # DB Connect
            conn, curs = self.dbConnect()
            # Write Query: Select Data
            sql = 'DELETE FROM ' + tableName
            # Execute Query
            curs.execute(sql)
            # Apply Query
            conn.commit()
        except:
            print('Error: Delete Failed')
        finally:
            # DB Close
            self.dbClose(curs, conn)
# -------------------------------------------------------------------------------------------------
