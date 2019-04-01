import tweepy # 트위피 사용하기 위함
import os # 크롤링 결과를 저장하기 위함
import pandas as pd # 크롤링한 데이터를 DataFrame 유형으로 저장

consumer_key = "MGRK5IsX8xwxhz0FYv5Llm5ps"  #API 키를 받아오기 위한 키
consumer_secret ="JRh3fHqPqEq6VWcyoKax6MG4nE21z0zatiDjEGnvmHm99cyrLA" #API 키를 받아오기 위한 비밀키
access_token ="1103843008670121984-qw1ooMrZLzK10AcQkuixvvq0dizVfR" # 앱에 접근이 가능하도록 하기 위한 토큰
access_token_secret= "dqplsyeDz5n7kkYB8kW6kIkDW7lPkoFnL3r4vpCR0brdJ" # 앱에 접근이 가능하도록 하기 위한 비밀 토큰

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # 핸들러 생성 및 개인정보 인증 요청
auth.set_access_token(access_token, access_token_secret) # 앱에 대한 액세스 요청 

api = tweepy.API(auth, wait_on_rate_limit=True)  #트위터 API 생성

results = [] # 결과값들을 저장하기 임시적으로 저장하기 위함
for tweet in tweepy.Cursor(api.search, q='버닝썬',since='2019-03-27', until='2019-03-29').items(5): #Cursor를 사용하여 search api를 사용함. 검색어는 버닝썬 날짜는 2019-03-27 부터 2019-03-26 23:59:59 까지, 10개의 트윗을 가져온다.
    
    results.append(tweet) # search로 찾은 결과를 results에 추가한다.
    
    print(results) # results 출력

def process_results(results): # 가져온 트윗들을 정리한다.
    id_list = [tweet.id for tweet in results] # results에 들어간 tweet 중 id를 id_list로 저장
    data_set = pd.DataFrame(id_list, columns=["id"]) #id_list 값을 ‘id’ 이름의 columns 로 저장하는 데이터프레임을 만든다.

    data_set["text"] = [tweet.text for tweet in results] # results에 들어간 tweet 중 text를 “text” 이름의 columns 로 추가 저장
    data_set["created_at"] = [tweet.created_at for tweet in results] # results에 들어간 tweet 중 created_at를  “text” 이름의 created_at 로 추가 저장
    data_set["retweet_count"] = [tweet.retweet_count for tweet in results] # results에 들어간 tweet 중 retweet_count를 “retweet_count” 이름의 columns 로 추가 저장
    data_set["favorite_count"] = [tweet.favorite_count for tweet in results] # results에 들어간 tweet 중 text를 “text” 이름의 columns 로 저장
    data_set["source"] = [tweet.source for tweet in results] # results에 들어간 tweet 중 source를 “source” 이름의 columns 로 추가 저장

data_set["user_id"] = [tweet.author.id for tweet in results] # results에 들어간 tweet 중 author.id를 “user_id” 이름의 columns 로 추가 저장
    data_set["user_screen_name"] = [tweet.author.screen_name for tweet in results] # results에 들어간 tweet 중 author.screen_name를 “user_screen_name” 이름의 columns 로 추가 저장
    data_set["user_name"] = [tweet.author.name for tweet in results] # results에 들어간 tweet 중 text를 “text” 이름의 columns 로 추가 저장
    data_set["user_created_at"] = [tweet.author.created_at for tweet in results]
    data_set["user_description"] = [tweet.author.description for tweet in results]
    data_set["user_followers_count"] = [tweet.author.followers_count for tweet in results]
    data_set["user_friends_count"] = [tweet.author.friends_count for tweet in results]
    data_set["user_location"] = [tweet.author.location for tweet in results]

    return data_set

data_set = process_results(results) #results 결과를 data_set에 저장
wfile = open(os.getcwd()+"/twitter.txt", mode='w', encoding='utf8') #twitter.txt 라는 파일에 읽기전용으로 저장한다.
data = {} 
i = 0 
for tweet in results:
    data['text'] = tweet.full_text #추출해낸 트윗들은 제한없이 저장할 수 있다.
    wfile.write(data['text']+'\n')
    i += 1
