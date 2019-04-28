'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
T-SA.py
      Title: T-SA의 기능 실행
     Author: Lee SeokJune
  Create on: 2019.04.08
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import TwitterAPI
import dbModule
import Visualization

# TwitterAPI, dbModule 관련 변수 설정 ---------------------------------------------------------------

# 서재익
statTwitter = ('MGRK5IsX8xwxhz0FYv5Llm5ps',                             # consumer_key
               'JRh3fHqPqEq6VWcyoKax6MG4nE21z0zatiDjEGnvmHm99cyrLA',    # consumer_secret
               '1103843008670121984-qw1ooMrZLzK10AcQkuixvvq0dizVfR',    # access_token
               'dqplsyeDz5n7kkYB8kW6kIkDW7lPkoFnL3r4vpCR0brdJ')         # access_token_secret
'''
# 이윤혁 
statTwitter = ('lNZwPI2dQ5l89K1nOGW6Sod6u',                             # consumer_key
               'D6eGld20D99yrL89SMYPhJsjiHqmNKGL5LznkNKOQQPoIoQxWA',    # consumer_secret
               '1107934597189263361-E83WGFw4XnDGpPkmYewJA7aIecHru6',    # access_token
               'CvbR5ga31iWxQVrWcnzdnp7NGBbmAFGWRntjuZbXnpAet')         # access_token_secret
'''
statKeyword = ('이윤혁',         # keyword
               '2019-04-25',    # sinceDate
               '2019-04-29',    # untilDate
               'extended',      # mode
               10)              # count
statUserInfo = ('BWnYuiJ0vkWsATq')  #screen_name / @으로 시작하는 이름
twitterDB = ('localhost',  # hostIP
          'T-SA',         # userID
          '1234',       # password
          'TWITTER',      # DB 종류
          'utf8')       # charset
visualDB = ('localhost',  # hostIP
          'T-SA',         # userID
          '1234',       # password
          'VISUAL',      # DB 종류
          'utf8')       # charset

tableName = ('KEYWORD_JSON',
             'KEYWORD_HASHTAG',
             'KEYWORD_METADATA',
             'KEYWORD_USER',
             'USER_JSON')


# TwitterAPI, dbModule 객체 생성 -------------------------------------------------------------------
twitter = TwitterAPI.TwitterAPI()
db = dbModule.dbModule(twitterDB[0],twitterDB[1],twitterDB[2],twitterDB[3],twitterDB[4])
db1 = dbModule.dbModule(visualDB[0],visualDB[1],visualDB[2],visualDB[3],visualDB[4])
visual = Visualization.Visualization()
#  TwitterAPI의 OAuth 실행 -------------------------------------------------------------------------
api = twitter.OAuth(statTwitter[0], statTwitter[1], statTwitter[2], statTwitter[3])

# 작동부 -------------------------------------------------------------------------------------------
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
    # 입력 오류 체크 --------------------------------------------------------------------------------
    if cNum not in ['1', '2', '3', '4']:
        print('Re-enter')
        continue
    # 종료 실행(4) ---------------------------------------------------------------------------------
    if cNum == '4':
        print('Exit!!')
        break
    # 작업할 테이블명 입력 후 데이터가 존재할 시 삭제 ---------------------------------------------------
    '''
    Modifier: Bae InGyu
    Modify on: 2019-04-09 
    작업할 테이블명 입력 후 데이터가 존재할 시 삭제하는 기능 추가 
    '''
    #table = input("작업할 테이블명 입력: ") 
    if db.getRowByCheck(tableName[1]) == True :
       print("========테이블에 존재4하는 데이터 삭제시작========")
       db.deleteDB(tableName[1])
    else :
       print("========테이블에 존재하는 데이터 없음========")
       
    '''
      기능 실행(1, 2, 3)
    '''
    # Keyword Search 실행(1) -----------------------------------------------------------------------
    if cNum == '1':
        print('Keyword Search 시작')
        # TwitterAPI.py 작업 -----------------------------------------------------------------------
        tweets = twitter.search_Keyword(api, statKeyword[0], statKeyword[1], statKeyword[2], statKeyword[3], statKeyword[4])
        keyword_Json, keyword_Hashtags, keyword_Metadata, keyword_User = twitter.result_Keyword(tweets)
        # dbModule.py 작업 -------------------------------------------------------------------------
        for val in keyword_Hashtags:
            db.insertDB('KEYWORD_HASHTAG', val)
        print(db.selectDB('KEYWORD_HASHTAG'))

        # -----------------------------------------------------------------------------------------
        print('Keyword Search 완료')
    # UserInfo Search 실행(2) --------------------------------------------------------------------------
    elif cNum == '2':
        print('UserInfo Search 시작')
        # TwitterAPI.py 작업 -----------------------------------------------------------------------
        userInfo = twitter.search_User(api, statUserInfo[0])
        user_Json = twitter.result_User(userInfo)
        # dbModule.py 작업 -------------------------------------------------------------------------
    



        
        # -----------------------------------------------------------------------------------------
        print('User Search 완료')
    # Visualization 실행(3) ------------------------------------------------------------------------
    elif cNum == '3':
        print('Visualization 시작')
        # Visualization.py 작업 --------------------------------------------------------------------
        hashtagCount = dict(db1.selectDB('HASHTAG'))
        visual.visualize(hashtagCount)
        # -----------------------------------------------------------------------------------------
        print('Visualization 완료')

