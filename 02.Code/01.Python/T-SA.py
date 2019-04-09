'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
T-SA.py
      Title: T-SA의 기능 실행
     Author: Lee SeokJune
  Create on: 2019.04.08
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''
 Modifier: Bae InGyu
Modify on: 2019-04-09 
dbModule.py 와 T-SA.py 적용시 필요한 설정 추가  
'''
import dbModule
#DB연결 파라미터 수정하는곳--------------------------------------------------------------------------
host = 'localhost' 
user = 'root'
pswd = '1234'
db   = 'mysql'
charset = 'utf8'

# dbModule.py 의 dbModule클래스생성 괄호안의 파라미터는 위에서 수정------------------------------------
db = dbModule.dbModule(host,user,pswd,db,charset) 

# insert values 변수(일단넣어둠)--------------------------------------------------------------------
values = " values(1,'Kim','010-0000-0001','Computer','A');" 


while True:
    '''
      기능 선택 입력 받기
      1. KeyWord Search
      2. User Search
      3. Visualization
      4. Exit
    '''
    print('1. Keyword Search')
    print('2. User Search')
    print('3. Visualization')
    print('4. Exit')
    print('Choice Number: ')
    cNum = input()

    # 입력 오류 체크 -------------------------------------------------------------------------------
    if cNum not in ['1', '2', '3', '4']:
        print('Re-enter')
        continue

    # 종료 실행(4) ---------------------------------------------------------------------------------
    if cNum == '4':
        print('Exit!!')
        break


    '''
     Modifier: Bae InGyu
    Modify on: 2019-04-09 
    작업할 테이블명 입력 후 데이터가 존재할 시 삭제하는 기능 추가 
    '''
    # 작업할 테이블명 입력 후 데이터가 존재할 시 삭제--------------------------------------------------
    table = input("작업할 테이블명 입력: ") 
    if db.getRowByCheck(table) == True :
       print("========기존에 있는 데이터 삭제시작========")
       db.deleteDB(table)




    '''
      기능 실행(1, 2, 3)
    '''
    # Keyword Search 실행(1) -----------------------------------------------------------------------
    if cNum == '1':
        print('Keyword Search 시작')
        # TwitterAPI.py 작업 -----------------------------------------------------------------------

        # dbModule.py 작업 -------------------------------------------------------------------------
        db.insertDB(table,values)
        print(db.selectDB(table))
        
        print('Keyword Search 완료')
    # User Search 실행(2) --------------------------------------------------------------------------
    elif cNum == '2':
        print('User Search 시작')
        # TwitterAPI.py 작업 -----------------------------------------------------------------------

        # dbModule.py 작업 -------------------------------------------------------------------------
        db.insertDB(table,values)
        print(db.selectDB(table))
        
        print('User Search 완료')
    # Visualization 실행(3) ------------------------------------------------------------------------
    elif cNum == '3':
        print('Visualization 시작')
        # Visualization.py 작업 --------------------------------------------------------------------
        
        print('Visualization 완료')

