'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

 dbMain.py
     Title: (dbModule을 불러와 실행한다.)
    Author: Bae In Gyu
 Create_at: 2019-04-02


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


import dbModule  # DBModule파일 -> (마리아DB접속 , 테이블조회 , 테이블삭제)  



#DB연결 파라미터 수정하는곳
host = 'localhost' 
user = 'root'
pswd = '1234'
db   = 'mysql'
charset = 'utf8'

db = dbModule.dbModule(host,user,pswd,db,charset)  # DB연결 파라미터 수정은 아래에서


# insert values 변수
values = " values(1,'Kim','010-0000-0001','Computer','A');" 


# 메인
table = input("\n테이블명 입력: ")      # 테이블명 입력받기
db.deleteDB(table)                     # 입력받은 테이블 데이터 삭제       
db.insertDB(table,values)              # 삭제후 데이터 삽입
print(db.selectDB(table))              # 삽입후 데이터 조회
