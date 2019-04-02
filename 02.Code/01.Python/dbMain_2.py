'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

 dbMain.py
     Title: (dbModule을 불러와 실행한다.)
    Author: Bae In Gyu
 Create_at: 2019-04-02
  Alter_at: 2019-04-03


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# DBModule파일 -> (마리아DB접속 , 테이블조회)   
import dbModule

# 조회할 테이블이름 입력 





table = input("조회할 테이블 입력: ") 
dbModule.dbModule.select(table) #테이블 조회
table = input("데이터 모두 삭제할 테이블 입력: ") 
dbModule.dbModule.delete(table)
 
