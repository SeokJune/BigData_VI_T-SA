'''
Title=Result output using 'user_timeline.API'
File name=user_timelineAPI.py
Writer=Seo JaeIck
Date of Creation=2019.04.02
Modified=2019.04.02

'''
from tweepy import Cursor
import tweepy 	    # 트위피 사용
import json	    # json 사용
from tweepy.auth import OAuthHandler

class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key=consumer_key
        self.consumer_secret=consumer_secret
        self.access_token=access_token
        self.access_token_secret=access_token_secret
        

    def OAuth(self, consumer_key, consumer_secret, access_token, access_token_secret):                
        auth=tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        global api
        api = tweepy.API(auth)
        print("인증되었습니다")

    def search(self, target, since_date, until_date):
      #  self.target = target
       # self.date = date
	
        cursor = tweepy.Cursor(self.api.search, q = target, since = since_date, until = until_date)

        return cursor.items(maxnu)
    
    
    def userInfo(self, username):
        info = tweepy.Cursor(self.api.get_user, screen_name=username)
        return info
    
    def test():
        ''' Test routine : Seo Ji-Su in Lovelyz '''
        consumerKey = "MGRK5IsX8xwxhz0FYv5Llm5ps"
        consumerSecret ="JRh3fHqPqEq6VWcyoKax6MG4nE21z0zatiDjEGnvmHm99cyrLA"
        accessToken ="1103843008670121984-qw1ooMrZLzK10AcQkuixvvq0dizVfR"
        accessTokenSecret= "dqplsyeDz5n7kkYB8kW6kIkDW7lPkoFnL3r4vpCR0brdJ"

        keyAuth=TwitterAPI(consumerKey,consumerSecret,accessToken,accessTokenSecret)
        keyAuth.OAuth(consumerKey,consumerSecret,accessToken,accessTokenSecret)

    
        list_tweets = api.search(target='버닝썬',since_date='2019-03-20', until_date='2019-03-30')
        
        print (list_tweets)
    
     #   for index, tweet in enumerate(list_tweets):
           
     #       print '<Info>', tweet.created_at, '| <Content>',
      #      print_unsafe(tweet.text.replace('\n', '\\n'))
       #    print


if __name__ == '__main__':
    TwitterAPI.test()

