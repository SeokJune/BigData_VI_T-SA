'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

 dbMain_3.py
     Title: (dbModule을 불러와 실행한다.)
    Author: Bae In Gyu
 Create_at: 2019-04-02


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



import dbModule_3  # DBModule파일 -> (마리아DB접속 , 테이블조회 , 테이블삭제)  


db = dbModule_3.dbModule_3('localhost','root','1234','mysql','utf8') # DB연결시 파라미터 여기서 수정
table = input("데이터 모두 조회할 테이블명 입력: ")  
print(db.selectDB(table))					     # 조회한 데이터 출력
table = input("데이터 모두 삭제할 테이블명 입력: ")  
db.deleteDB(table)						     # 테이블의 데이터 모두 삭제
