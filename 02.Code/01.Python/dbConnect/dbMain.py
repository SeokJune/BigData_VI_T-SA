'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

 dbMain.py
     Title: (dbModule을 불러와 실행한다.)
    Author: Bae In Gyu
 Create_at: 2019-04-02


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



import dbModule  # DBModule파일 -> (마리아DB접속 , 테이블조회 , 테이블삭제)  

# DB연결시 파라미터 수정하는곳
host = 'localhost' 
user = 'root'
pswd = '1234'
db   = 'mysql'
charset = 'utf8'

values = " values(1,'Kim','010-0000-0001','Computer','A');"

db = dbModule.dbModule(host,user,pswd,db,charset)        # DB연결시 파라미터수정은 위에 변수에서
table = input("\n데이터 모두 조회할 테이블명 입력: ")  
print(db.selectDB(table))
db.getCodeByCheck(table)				     # 조회한 데이터 출력
table = input("\n데이터 모두 삭제할 테이블명 입력: ")  
db.deleteDB(table)
db.getCodeByCheck(table)				     # 테이블의 데이터 모두 삭제
table = input("\n데이터 삽입할 테이블명 입력: ")
db.insertDB(table,values)
db.getCodeByCheck(table)


