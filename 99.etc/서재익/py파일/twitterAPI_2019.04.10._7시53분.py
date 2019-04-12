'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
twitterAPI.py
      Title: tweepy API의 기능 실행 및 결과값 저장
     Author: Seo JaeIck
  Create on: 2019.04.03
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import numpy as np
import tweepy
import pandas as pd
from tweepy import OAuthHandler, api

    
class TwitterAPI:
    def __init__(self,ck,cs,at,ats):
        self.consumer_key = ck
        self.consumer_secret = cs
        self.access_token = at
        self.access_token_secret = ats 
'''
Modifier: Seo JaeIck
Modify on: 2019.04.07.
클래스 이름 변경

class TwitterClient :
'''
    #트위피 API 인증''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def OAuth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api=tweepy.API(auth)
        
        return api
'''
Modifier: Seo JaeIck
Modify on: 2019.04.09.
global 삭제

    def OAuth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        global api
        api = tweepy.API(auth)
'''    
    #단어로 트윗 검색''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    def keySearch(self, keyword, sinceD, untilD, count):
        api=self.OAuth()
        self.keyword = keyword
        self.sinceD=sinceD
        self.untilD=untilD
        tweets=[]
        try:
        	for tweet in tweepy.Cursor(api.search, q = self.keyword, since=sinceD, until=untilD, tweet_moede='extended').items(count):
        		tweets.append(tweet)      
                      
        except tweepy.error.TweepError:
        	print("트위피 제한에 도달")  
        	          
        return tweets
'''
Modifier: Seo JaeIck
Modify on: 2019.04.09.
api=TwitterAPI.OAuth 추가, 예외 선언

    def keySearch(self, keyword, sinceD, untilD, count=5):
        self.OAuth()
        self.keyword = keyword
        self.sinceD=sinceD
        self.untilD=untilD
        tweets=[]
        for tweet in tweepy.Cursor(api.search, q = self.keyword, since=sinceD, until=untilD, tweet_moede='extended').items(count):
            tweets.append(tweet)
            
        return tweets
'''               
                   
    #사용자 이름으로 사용자 정보 검색''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def userInfo(self, username):
        self.OAuth()
        self.username=username
        api=TwitterAPI.OAuth(self)         
        user=api.get_user(self.username)
        
        return user
    
'''
Modifier: Seo JaeIck
Modify on: 2019.04.09.
global 삭제

    def UserInfo(self, username):
        self.OAuth()
        self.username=username
        
        global user
        user=api.get_user(self.username)
'''
    
    #검색에 대한 결과값을 데이터프레임으로 저장''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def keyword_result(self, tweets):
        self.OAuth()
        df = pd.DataFrame()     

        df["id"]   = np.array([tweet.id for tweet in tweets])
        df["text"] = np.array([tweet.text for tweet in tweets])
        df['id_str'] = np.array([tweet.id_str for tweet in tweets])
        df['entities'] = np.array([tweet.entities for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['in_reply_to_status_id'] = np.array([tweet.in_reply_to_status_id for tweet in tweets])
        df['in_reply_to_status_id_str'] = np.array([tweet.in_reply_to_status_id_str for tweet in tweets])
        df['in_reply_to_user_id'] = np.array([tweet.in_reply_to_user_id for tweet in tweets])
        df['in_reply_to_user_id_str'] = np.array([tweet.in_reply_to_user_id_str for tweet in tweets])
        df['in_reply_to_screen_name'] = np.array([tweet.in_reply_to_screen_name for tweet in tweets])
        df['user_name'] = np.array([tweet.user.name for tweet in tweets])
        df['user_id'] = np.array([tweet.user.id for tweet in tweets])
        df['user_id_str'] = np.array([tweet.user.id_str for tweet in tweets])
        df['screen_name'] = np.array([tweet.user.screen_name for tweet in tweets])
        df['location'] = np.array([tweet.user.location for tweet in tweets])
        df['description'] = np.array([tweet.user.description for tweet in tweets])
        df['url'] = np.array([tweet.user.url for tweet in tweets])
        df['uesr_entities'] = np.array([tweet.entities for tweet in tweets])
        df['protected'] = np.array([tweet.user.protected for tweet in tweets])
        df['followers_count'] = np.array([tweet.user.followers_count for tweet in tweets])
        df['friends_count'] = np.array([tweet.user.friends_count for tweet in tweets])
        df['listed_count'] = np.array([tweet.user.listed_count for tweet in tweets])
        df['user_created'] = np.array([tweet.user.created_at for tweet in tweets])
        df['favourites_count'] = np.array([tweet.user.favourites_count for tweet in tweets])
        df['utc_offset'] = np.array([tweet.user.utc_offset for tweet in tweets])
        df['time_zone'] = np.array([tweet.user.time_zone for tweet in tweets])
        df['geo_enabled'] = np.array([tweet.user.geo_enabled for tweet in tweets])
        df['verified'] = np.array([tweet.user.verified for tweet in tweets])
        df['statuses_count'] = np.array([tweet.user.statuses_count for tweet in tweets])
        df['user_lang'] = np.array([tweet.user.lang for tweet in tweets])
        df['contributors_enabled'] = np.array([tweet.user.contributors_enabled for tweet in tweets])
        df['is_translator'] = np.array([tweet.user.is_translator for tweet in tweets])
        df['profile_background_color'] = np.array([tweet.user.profile_background_color for tweet in tweets])
        df['profile_background_image_url'] = np.array([tweet.user.profile_background_image_url for tweet in tweets])
        df['profile_background_image_url_https'] = np.array([tweet.user.profile_background_image_url_https for tweet in tweets])
        df['profile_background_tile'] = np.array([tweet.user.profile_background_tile for tweet in tweets])
        df['profile_image_url'] = np.array([tweet.user.profile_image_url for tweet in tweets])
        df['profile_image_url_https'] = np.array([tweet.user.profile_image_url_https for tweet in tweets])
        df['profile_link_color'] = np.array([tweet.user.profile_link_color for tweet in tweets])
        df['profile_sidebar_border_color'] = np.array([tweet.user.profile_sidebar_border_color for tweet in tweets])
        df['profile_sidebar_fill_color'] = np.array([tweet.user.profile_sidebar_fill_color for tweet in tweets])
        df['profile_text_color'] = np.array([tweet.user.profile_text_color for tweet in tweets])
        df['profile_use_background_image'] = np.array([tweet.user.profile_use_background_image for tweet in tweets])
        df['has_extended_profile'] = np.array([tweet.user.has_extended_profile for tweet in tweets])
        df['default_profile'] = np.array([tweet.user.default_profile for tweet in tweets])
        df['default_profile_image'] = np.array([tweet.user.default_profile_image for tweet in tweets])
        df['following'] = np.array([tweet.user.following for tweet in tweets])
        df['follow_request_sent'] = np.array([tweet.user.follow_request_sent for tweet in tweets])
        df['notifications'] = np.array([tweet.user.notifications for tweet in tweets])
        df['translator_type'] = np.array([tweet.user.translator_type for tweet in tweets])
        df['geo'] = np.array([tweet.geo for tweet in tweets])
        df['coordinates'] = np.array([tweet.coordinates for tweet in tweets])
        df['place'] = np.array([tweet.place for tweet in tweets])
        df['contributors'] = np.array([tweet.contributors for tweet in tweets])
        df['is_quote_status'] = np.array([tweet.is_quote_status for tweet in tweets])
        df['retweet_count'] = np.array([tweet.retweet_count for tweet in tweets])
        df['favorite_count'] = np.array([tweet.favorite_count for tweet in tweets])
        df['favorited'] = np.array([tweet.favorited for tweet in tweets])
        df['retweeted'] = np.array([tweet.retweeted for tweet in tweets])
        df['lang'] = np.array([tweet.lang for tweet in tweets])
        df['created_at'] = np.array([tweet.created_at for tweet in tweets])
        
        return df
'''
Modifier: Seo JaeIck
Modify on: 2019.04.09.
self.auth() 추가

   def result_tweet(self, tweets):
        df = pd.DataFrame()     

        df["id"]   = np.array([tweet.id for tweet in tweets])
        df["text"] = np.array([tweet.text for tweet in tweets])
        df['id_str'] = np.array([tweet.id_str for tweet in tweets])
        df['entities'] = np.array([tweet.entities for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['in_reply_to_status_id'] = np.array([tweet.in_reply_to_status_id for tweet in tweets])
        df['in_reply_to_status_id_str'] = np.array([tweet.in_reply_to_status_id_str for tweet in tweets])
        df['in_reply_to_user_id'] = np.array([tweet.in_reply_to_user_id for tweet in tweets])
        df['in_reply_to_user_id_str'] = np.array([tweet.in_reply_to_user_id_str for tweet in tweets])
        df['in_reply_to_screen_name'] = np.array([tweet.in_reply_to_screen_name for tweet in tweets])
        df['user_name'] = np.array([tweet.user.name for tweet in tweets])
        df['user_id'] = np.array([tweet.user.id for tweet in tweets])
        df['user_id_str'] = np.array([tweet.user.id_str for tweet in tweets])
        df['screen_name'] = np.array([tweet.user.screen_name for tweet in tweets])
        df['location'] = np.array([tweet.user.location for tweet in tweets])
        df['description'] = np.array([tweet.user.description for tweet in tweets])
        df['url'] = np.array([tweet.user.url for tweet in tweets])
        df['uesr_entities'] = np.array([tweet.entities for tweet in tweets])
        df['protected'] = np.array([tweet.user.protected for tweet in tweets])
        df['followers_count'] = np.array([tweet.user.followers_count for tweet in tweets])
        df['friends_count'] = np.array([tweet.user.friends_count for tweet in tweets])
        df['listed_count'] = np.array([tweet.user.listed_count for tweet in tweets])
        df['user_created'] = np.array([tweet.user.created_at for tweet in tweets])
        df['favourites_count'] = np.array([tweet.user.favourites_count for tweet in tweets])
        df['utc_offset'] = np.array([tweet.user.utc_offset for tweet in tweets])
        df['time_zone'] = np.array([tweet.user.time_zone for tweet in tweets])
        df['geo_enabled'] = np.array([tweet.user.geo_enabled for tweet in tweets])
        df['verified'] = np.array([tweet.user.verified for tweet in tweets])
        df['statuses_count'] = np.array([tweet.user.statuses_count for tweet in tweets])
        df['user_lang'] = np.array([tweet.user.lang for tweet in tweets])
        df['contributors_enabled'] = np.array([tweet.user.contributors_enabled for tweet in tweets])
        df['is_translator'] = np.array([tweet.user.is_translator for tweet in tweets])
        df['profile_background_color'] = np.array([tweet.user.profile_background_color for tweet in tweets])
        df['profile_background_image_url'] = np.array([tweet.user.profile_background_image_url for tweet in tweets])
        df['profile_background_image_url_https'] = np.array([tweet.user.profile_background_image_url_https for tweet in tweets])
        df['profile_background_tile'] = np.array([tweet.user.profile_background_tile for tweet in tweets])
        df['profile_image_url'] = np.array([tweet.user.profile_image_url for tweet in tweets])
        df['profile_image_url_https'] = np.array([tweet.user.profile_image_url_https for tweet in tweets])
        df['profile_link_color'] = np.array([tweet.user.profile_link_color for tweet in tweets])
        df['profile_sidebar_border_color'] = np.array([tweet.user.profile_sidebar_border_color for tweet in tweets])
        df['profile_sidebar_fill_color'] = np.array([tweet.user.profile_sidebar_fill_color for tweet in tweets])
        df['profile_text_color'] = np.array([tweet.user.profile_text_color for tweet in tweets])
        df['profile_use_background_image'] = np.array([tweet.user.profile_use_background_image for tweet in tweets])
        df['has_extended_profile'] = np.array([tweet.user.has_extended_profile for tweet in tweets])
        df['default_profile'] = np.array([tweet.user.default_profile for tweet in tweets])
        df['default_profile_image'] = np.array([tweet.user.default_profile_image for tweet in tweets])
        df['following'] = np.array([tweet.user.following for tweet in tweets])
        df['follow_request_sent'] = np.array([tweet.user.follow_request_sent for tweet in tweets])
        df['notifications'] = np.array([tweet.user.notifications for tweet in tweets])
        df['translator_type'] = np.array([tweet.user.translator_type for tweet in tweets])
        df['geo'] = np.array([tweet.geo for tweet in tweets])
        df['coordinates'] = np.array([tweet.coordinates for tweet in tweets])
        df['place'] = np.array([tweet.place for tweet in tweets])
        df['contributors'] = np.array([tweet.contributors for tweet in tweets])
        df['is_quote_status'] = np.array([tweet.is_quote_status for tweet in tweets])
        df['retweet_count'] = np.array([tweet.retweet_count for tweet in tweets])
        df['favorite_count'] = np.array([tweet.favorite_count for tweet in tweets])
        df['favorited'] = np.array([tweet.favorited for tweet in tweets])
        df['retweeted'] = np.array([tweet.retweeted for tweet in tweets])
        df['lang'] = np.array([tweet.lang for tweet in tweets])
        df['created_at'] = np.array([tweet.created_at for tweet in tweets])
        
        return df
'''    
    
    # 사용자 정보에대한 결과값을 데이터프레임으로 저장'''''''''''''''''''''''''''''''''''''''''''''''''''''

    def user_result(self, tweets):
        user=TwitterAPI.userInfo(self, username)
        df = pd.DataFrame()
 
        df["id"] = np.array([user.id])
        df["id_str"] = np.array([user.id_str])
        df["name"] = np.array([user.name])
        df["screen_name"] = np.array([user.screen_name])
        df["location"] = np.array([user.location])
        df["description"] = np.array([user.description])
        df["url"] = np.array([user.url])
        df["entities"] = np.array([user.entities])
        df["protected"] = np.array([user.protected])
        df["followers_count"] = np.array([user.followers_count])
        df["friends_count"] = np.array([user.friends_count])
        df["listed_count"] = np.array([user.listed_count])
        df["created_at"] = np.array([user.created_at])
        df["favourites_count"] = np.array([user.favourites_count])
        df["time_zone"] = np.array([user.time_zone])
        df["geo_enabled"] = np.array([user.geo_enabled])
        df["verified"] = np.array([user.verified])
        df["lang"] = np.array([user.lang])
        df["contributors_enabled"] = np.array([user.contributors_enabled])
        df["is_translator"] = np.array([user.is_translator])
        df["profile_background_color"] = np.array([user.profile_background_color])
        df["profile_background_image_url"] = np.array([user.profile_background_image_url])
        df["profile_background_image_url_https"] = np.array([user.profile_background_image_url_https])
        df["profile_background_tile"] = np.array([user.profile_background_tile])
        df["profile_image_url"] = np.array([user.profile_image_url])
        df["profile_image_url_https"] = np.array([user.profile_image_url_https])
        df["profile_link_color"] = np.array([user.profile_link_color])
        df["profile_sidebar_border_color"] = np.array([user.profile_sidebar_border_color])
        df["profile_text_color"] = np.array([user.profile_text_color])
        df["profile_use_background_image"] = np.array([user.profile_use_background_image])
        df["has_extended_profile"] = np.array([user.has_extended_profile])
        df["default_profile"] = np.array([user.default_profile])
        df["default_profile_image"] = np.array([user.default_profile_image])
        df["following"] = np.array([user.following])
        df["follow_request_sent"] = np.array([user.follow_request_sent])
        df["notifications"] = np.array([user.notifications])
        df["translator_type"] = np.array([user.translator_type])
        df["statuses_count"] = np.array([user.statuses_count])
        
        return df
'''
Modifier: Seo JaeIck
Modify on: 2019.04.09.
user=TwitterAPI.userInfo(self, username) 추가

   def result_tweet2(self, tweets):               
        df = pd.DataFrame()
 
        df["id"] = np.array([user.id])
        df["id_str"] = np.array([user.id_str])
        df["name"] = np.array([user.name])
        df["screen_name"] = np.array([user.screen_name])
        df["location"] = np.array([user.location])
        df["description"] = np.array([user.description])
        df["url"] = np.array([user.url])
        df["entities"] = np.array([user.entities])
        df["protected"] = np.array([user.protected])
        df["followers_count"] = np.array([user.followers_count])
        df["friends_count"] = np.array([user.friends_count])
        df["listed_count"] = np.array([user.listed_count])
        df["created_at"] = np.array([user.created_at])
        df["favourites_count"] = np.array([user.favourites_count])
        df["time_zone"] = np.array([user.time_zone])
        df["geo_enabled"] = np.array([user.geo_enabled])
        df["verified"] = np.array([user.verified])
        df["lang"] = np.array([user.lang])
        df["contributors_enabled"] = np.array([user.contributors_enabled])
        df["is_translator"] = np.array([user.is_translator])
        df["profile_background_color"] = np.array([user.profile_background_color])
        df["profile_background_image_url"] = np.array([user.profile_background_image_url])
        df["profile_background_image_url_https"] = np.array([user.profile_background_image_url_https])
        df["profile_background_tile"] = np.array([user.profile_background_tile])
        df["profile_image_url"] = np.array([user.profile_image_url])
        df["profile_image_url_https"] = np.array([user.profile_image_url_https])
        df["profile_link_color"] = np.array([user.profile_link_color])
        df["profile_sidebar_border_color"] = np.array([user.profile_sidebar_border_color])
        df["profile_text_color"] = np.array([user.profile_text_color])
        df["profile_use_background_image"] = np.array([user.profile_use_background_image])
        df["has_extended_profile"] = np.array([user.has_extended_profile])
        df["default_profile"] = np.array([user.default_profile])
        df["default_profile_image"] = np.array([user.default_profile_image])
        df["following"] = np.array([user.following])
        df["follow_request_sent"] = np.array([user.follow_request_sent])
        df["notifications"] = np.array([user.notifications])
        df["translator_type"] = np.array([user.translator_type])
        df["statuses_count"] = np.array([user.statuses_count])
        
        return df

'''           


'''
Modifier: Seo JaeIck
Modify on: 2019.04.09.
Search API와 get_user API의 결과를 합친 allResult 추가
allResult 삭제
'''
'''
    def allResult(self):
        tweets1=self.keySearch(keyword, sinceD, untilD, count)
        df1=self.keyword_result(tweets1)
        keys1=tuple(df1.keys())
        values1=tuple(df1.values)
        keyValue1=(keys1, values1)
        
        tweets2=self.userInfo(username)
        df2=self.user_result(tweets2)
        keys2=tuple(df2.keys())
        values2=tuple(df2.values)
        keyValue2=(keys2, values2)
        
        allKeyValue=(keyValue1, keyValue2)

'''        


'''
Modifier=Seo JaeIck
modify on=2019.04.07
키 값을 불러오고, 검색 조건을 입력하고, 결과값들을 출력하는 부분을 주석처리

'''
'''
ck = "MGRK5IsX8xwxhz0FYv5Llm5ps"
cs = "JRh3fHqPqEq6VWcyoKax6MG4nE21z0zatiDjEGnvmHm99cyrLA"
at = "1103843008670121984-qw1ooMrZLzK10AcQkuixvvq0dizVfR" 
ats = "dqplsyeDz5n7kkYB8kW6kIkDW7lPkoFnL3r4vpCR0brdJ" 


keyword="버닝썬"
sinceD="2019-03-20"
untilD="2019-04-04"
count=10
username="realDonaldTrump"
    
s = TwitterAPI(ck,cs,at,ats)     # 클래스 생성자
s.OAuth                      # 클래스의 OAuth()함수 호출

tweets1=s.keySearch(keyword, sinceD, untilD, count)
df1=s.keyword_result(tweets1)
keys1=tuple(df1.keys())
values1=tuple(df1.values)
keyValue1=(keys1, values1)

tweets2=s.userInfo(username)
df2=s.user_result(tweets2)
keys2=tuple(df2.keys())
values2=tuple(df2.values)
keyValue2=(keys2, values2)

allKeyValue=(keyValue1, keyValue2)


#print(df1)                 #키워드를 통한 검색 결과 출력
#print(df2)                 #사용자 이름을 통한 사용자 정보 출력
#print(keyValue1)           #키워드 검색의 결과    
#print(keyValue2)           #사용자 정보의 결과
#print(allKeyValue)         #키워드 검색과 사용자 정보 결과를 합침
                                #((키워드 전체 칼럼, 키워드 칼럼의 값),(사용자 정보 전체 칼럼, 사용자 칼럼의 값))
'''	







'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Writer=Seo JaeIck
modified=2019.04.07
수정 내용 : 기존 코드 중에서, 인증 받는 TwitterClient와 분석하는 TweetAnalyzer로 클래스화 시켜서 작업 진행.

import numpy as np
import tweepy
import pandas as pd
from tweepy import OAuthHandler

class TwitterClient :
    def __init__(self,ck,cs,at,ats):
        self.consumer_key = ck
        self.consumer_secret = cs
        self.access_token = at
        self.access_token_secret = ats 

    # tweepy 인증
    def TweepyAuth(self) :

        global api
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

    # tweepy인증 함수 불러와서 인증하고 keyword검색 후 데이터 프레임에 넣고 리턴하기

    def keywordSearch(self,keyword,count) :
        self.TweepyAuth()
        self.keyword = keyword
        self.count = count
        result = []  
        for tweet in tweepy.Cursor(api.search, q = self.keyword,count = self.count).items():
                     result.append(tweet)

        data_set = pd.DataFrame()     
        data_set["id"]   = [tweet.id for tweet in result]
        data_set["text"] = [tweet.text for tweet in result]

        return data_set

    def get_tweets(self, query, since_date, until_date, count = 10):
        tweets = []

        tweet = self.api.search(q = query, since=since_date, until=until_date, count = count)
        tweets.append(tweet)
        return tweets
    
    def user_Information(self, username):
        info=[]
        
        #info list에 결과값들을 저장.
        information=self.api.get_user(screen_name=username)
        info.append(information)
        return info

class TweetAnalyzer():  #가져온 트윗을 분석하기 위한
    def tweet_dataframe(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        
        df['id'] = np.array([tweet.id for tweet in tweets])
   
        return df

if __name__ == "__main__":
    api = TwitterClient()
    analyze=TweetAnalyzer()
    tweeting = api.get_tweets(query = 'python', since_date='2018-03-03', until_date='2019-04-04', count = 1)
    df=analyze.tweet_dataframe(tweeting)
    print(df)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''




'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Writer=Seo JaeIck
modified=2019.04.02
수정 내용 : 각 


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


message = 트윗 내용 저장, favorite_count = 좋아요 갯수, retweet_count = 리트윗 횟수, created_at = 글 작성 날짜
user_name = 사용자 이름, favourites_count= 좋아요 누른 횟수, description = 계정 소개, friends_count = 친구 수, followers_count=나를 팔로워한 수
Cursor를 써서 tweepy의 search를 가져온다.
q= 찾을 단어, since= 찾으려는 시작 날짜, until= 찾으려는 끝 날짜 tweet_mode='extended' => 트윗의 제한을 헤제한다, count=횟수
이후 데이터 프레임을 만들어서 각 값들을 집어넣는다.

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


message = 트윗 내용 저장, favorite_count = 좋아요 갯수, retweet_count = 리트윗 횟수, created_at = 글 작성 날짜
user_name = 사용자 이름, favourites_count= 좋아요 누른 횟수, description = 계정 소개, friends_count = 친구 수, followers_count=나를 팔로워한 수
Cursor를 써서 tweepy의 user_timeline을 가져온다.
screen_name = 계정 이름, since= 찾으려는 시작 날짜, until= 찾으려는 끝 날짜 tweet_mode='extended' => 트윗의 제한을 헤제한다, count=횟수
이후 데이터 프레임을 만들어서 각 값들을 집어넣는다.

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

파일 저장 방법
wfile = open(os.getcwd()+"/user_timeline.txt", mode='w', encoding='utf8')
data = {}
i = 0
for tweet in results:
    data['text'] = tweet.full_text
    wfile.write(data['text']+'\n')
    i += 1

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

