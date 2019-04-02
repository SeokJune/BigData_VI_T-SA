'''
Title=Result output using 'user_timeline.API'
File name=user_timelineAPI.py
Writer=Seo JaeIck
Date of Creation=2019.04.02
Modified=2019.04.02

'''

import tweepy 	    # 트위피 사용
import pandas as pd # 데이터프레임 제작시 사용
import json	    # json 사용

consumer_key = "MGRK5IsX8xwxhz0FYv5Llm5ps" # API를 받아오기 위한 키
consumer_secret ="JRh3fHqPqEq6VWcyoKax6MG4nE21z0zatiDjEGnvmHm99cyrLA" # API를 받아오기 위한 비밀키
access_token ="1103843008670121984-qw1ooMrZLzK10AcQkuixvvq0dizVfR"    # 앱 접근 허용을 하기위한 토큰
access_token_secret= "dqplsyeDz5n7kkYB8kW6kIkDW7lPkoFnL3r4vpCR0brdJ"  # 앱 접근 허용을 하기위한 비밀토큰

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # 키를 이용한 인증
auth.set_access_token(access_token, access_token_secret)  # 토큰을 이용한 접근 허가

api = tweepy.API(auth)  # API 등록

userid=[]  # 찾으려는 아이디를 저장
count=''   # 찾으려는 개수를 저장
ymd1=[]    # 찾으려는 날짜 시작일
ymd2=[]    # 찾으려는 날짜 종료일
keyword=[] # 찾으려는 단어 저장
woeidnum=[]# 찾으려는 WOEID 번호 저장

woeidnum=input("나라를 찾기위해서 WOEID 번호를 입력하세요(한국은 '23424868') :")
trends1 = api.trends_place(woeidnum) 		# 대한민국의 WOEID 번호를 입력
data = trends1[0]				
trends = data['trends']				# 검색을 통한 트렌드 값을 data에 저장
names = [trend['name'] for trend in trends] 	# trend에 있는 name 들만 따로 names로 지정
trendsName = ' '.join(names) 			# 분리된 문장은 ''로 이어준다

df = pd.DataFrame(names, columns=["name"])# 가져온 names를 데이터 프레임에 집어넣는다. 이때 그 column의 이름이 'names'

#데이터프레임 출력과 다음 API와 구분하기 위함
print(df) 
print ('********************'+'\n'+'\n')


keyword=input("찾으려는 검색어를 입력하세요 :")			     #검색어 입력
ymd1=input("찾으려는 날짜의 시작일을 입력하세요(공백없이 , 로 구분) : ")  #시작 날짜 입력
ymd2=input("찾으려는 날짜의 종료일을 입력하세요(공백없이 , 로 구분) : ")  #종료 날짜 입력
count=int(input("찾으려는 갯수를 입력하세요 : ")) 		     #갯수입력
ymd1=ymd1.split(',') #입력값 ',' 로 분리
ymd2=ymd2.split(',') #입력값 ',' 로 분리
sdate='-'.join(ymd1) #분리된 값들 '-'로 이어줌
udate='-'.join(ymd2) #분리된 값들 '-'로 이어줌

results = []  #결과값들 임시 저장

'''
message = 트윗 내용 저장, favorite_count = 좋아요 갯수, retweet_count = 리트윗 횟수, created_at = 글 작성 날짜
user_name = 사용자 이름, favourites_count= 좋아요 누른 횟수, description = 계정 소개, friends_count = 친구 수, followers_count=나를 팔로워한 수
Cursor를 써서 tweepy의 search를 가져온다.
q= 찾을 단어, since= 찾으려는 시작 날짜, until= 찾으려는 끝 날짜 tweet_mode='extended' => 트윗의 제한을 헤제한다, count=횟수
이후 데이터 프레임을 만들어서 각 값들을 집어넣는다.

'''
message,favorite_count,retweet_count,created_at,user_name,favourites_count,description,friends_count,followers_count=[],[],[],[],[],[],[],[],[]
for tweet in tweepy.Cursor(api.search, q=keyword, since=sdate, until=udate, tweet_mode='extended').items(count):
    results.append(json.dumps(tweet._json))
    content=tweet.full_text

    message.append(tweet.full_text)
    favorite_count.append(tweet.favorite_count)
    retweet_count.append(tweet.retweet_count)
    created_at.append(tweet.created_at)
    user_name.append(tweet.user.name)
    favourites_count.append(tweet.user.favourites_count)
    description.append(tweet.user.description)
    friends_count.append(tweet.user.friends_count)
    followers_count.append(tweet.user.followers_count)


df=pd.DataFrame({'Message':message,
                'Tweet Favorite Count':favorite_count,
                'Retweet Count':retweet_count,
                'Created At':created_at,
                'Username':user_name,
                'Likes':favourites_count,
                'User Description':description,
                'Following':friends_count,
                'Followers':followers_count})

print(df)
print ('********************'+'\n'+'\n')

userid=input("사용자 ID를 입력하세요 :") 				     #아이디 입력
ymd1=input("찾으려는 날짜의 시작일을 입력하세요(공백없이 , 로 구분) : ")  #시작 날짜 입력
ymd2=input("찾으려는 날짜의 종료일을 입력하세요(공백없이 , 로 구분) : ")  #종료 날짜 입력
count=int(input("찾으려는 갯수를 입력하세요 : ")) 		     #갯수입력
ymd1=ymd1.split(',') #입력값 ',' 로 분리
ymd2=ymd2.split(',') #입력값 ',' 로 분리
sdate='-'.join(ymd1) #분리된 값들 '-'로 이어줌
udate='-'.join(ymd2) #분리된 값들 '-'로 이어줌

results = []  #결과값들 임시 저장

'''
message = 트윗 내용 저장, favorite_count = 좋아요 갯수, retweet_count = 리트윗 횟수, created_at = 글 작성 날짜
user_name = 사용자 이름, favourites_count= 좋아요 누른 횟수, description = 계정 소개, friends_count = 친구 수, followers_count=나를 팔로워한 수
Cursor를 써서 tweepy의 user_timeline을 가져온다.
screen_name = 계정 이름, since= 찾으려는 시작 날짜, until= 찾으려는 끝 날짜 tweet_mode='extended' => 트윗의 제한을 헤제한다, count=횟수
이후 데이터 프레임을 만들어서 각 값들을 집어넣는다.

'''
message,favorite_count,retweet_count,created_at,user_name,favourites_count,description,friends_count,followers_count=[],[],[],[],[],[],[],[],[]
for tweet in tweepy.Cursor(api.user_timeline, screen_name=userid, since=sdate, until=udate, tweet_mode='extended').items(count):
    results.append(json.dumps(tweet._json))
    content=tweet.full_text

    message.append(tweet.full_text)
    favorite_count.append(tweet.favorite_count)
    retweet_count.append(tweet.retweet_count)
    created_at.append(tweet.created_at)
    user_name.append(tweet.user.name)
    favourites_count.append(tweet.user.favourites_count)
    description.append(tweet.user.description)
    friends_count.append(tweet.user.friends_count)
    followers_count.append(tweet.user.followers_count)

df=pd.DataFrame({'Message':message,
                'Tweet Favorite Count':favorite_count,
                'Retweet Count':retweet_count,
                'Created At':created_at,
                'Username':user_name,
                'Likes':favourites_count,
                'User Description':description,
                'Following':friends_count,
                'Followers':followers_count})


print(df)


#df.to_csv("Twitter Timeline.csv")
#데이터프레임을 data_set에 저장
#data_set = process_results(results)

#데이터프레임 출력
#print(data_set.head()) 
'''
파일 저장 방법
wfile = open(os.getcwd()+"/user_timeline.txt", mode='w', encoding='utf8')
data = {}
i = 0
for tweet in results:
    data['text'] = tweet.full_text
    wfile.write(data['text']+'\n')
    i += 1

'''
