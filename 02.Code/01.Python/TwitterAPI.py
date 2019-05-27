# TwitterAPI.py
#  Title: Collect Twitter Data, Data preprocessing
# Author: Lee SeokJune
# --------------------------------------------------------------------------------------------------
# import module
# --------------------------------------------------------------------------------------------------
## Base64 is a way in which 8-bit binary data is encoded into a format that can be represented in 7 bit.
import base64   # Using by 'encodeKey'
## Module sending HTTP request
import requests # Using by 'getAuthResponse'
# --------------------------------------------------------------------------------------------------
#  Class Name: TwitterAPI
# Method list: Generator
#            : encodeKey, getAuthResponse
#            : searchTweet, searchTimeline
#            : preprocess
# --------------------------------------------------------------------------------------------------
class TwitterAPI:
    # ----------------------------------------------------------------------------------------------
    # Generator
    # Set: baseUrl, mapMonth
    # ----------------------------------------------------------------------------------------------
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        # Drictionary for converting Alphabetic into Number
        self.mapMonth = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05','Jun':'06',
                         'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11','Des':'12'}
    # ----------------------------------------------------------------------------------------------
    # Encode: clientKey, clientSecret
    # ----------------------------------------------------------------------------------------------
    def encodeKey(self, clientKey, clientSecret):
        # Change 'clientKey' and 'clientSecret' to formatting '{}:{}'
        # Character encoding type is ASCII(American Standard Code for Information Interchange)
        keySecret = '{}:{}'.format(clientKey, clientSecret).encode('ascii')
        # Encoding 'keySecret' through Base64.b64encode()
        b64EncodedKey = base64.b64encode(keySecret)
        # Decoding 'b64EncodedKey' through Str.decode()
        b64EncodedKey = b64EncodedKey.decode('ascii')
        # 'b64EncodedKey' return
        return b64EncodedKey
    # ----------------------------------------------------------------------------------------------
    # Get Auth Response
    # ----------------------------------------------------------------------------------------------
    def getAuthResponse(self, b64_encoded_key):
        # Set URL
        authUrl = '{}oauth2/token'.format(self.baseUrl)
        # Set Header: Authorization, Content-Type
        authHeaders = { 'Authorization': 'Basic {}'.format(b64_encoded_key),
                         'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' }
        # Set Data: grant_type
        authData = { 'grant_type': 'client_credentials' }
        # POST Transmission Method(URL, header, data)
        authResponse = requests.post(authUrl, headers = authHeaders, data = authData)
        # 'authResponse' return
        return authResponse
    # ----------------------------------------------------------------------------------------------
    #  Get Search Tweets(Return Type: list)
    # ----------------------------------------------------------------------------------------------
    def searchTweet(self, authResponse, devEnvironmentLabel, query, fromDate, toDate, maxResults):
        # Set URL
        searchUrl = '{}1.1/tweets/search/fullarchive/{}.json'.format(self.baseUrl, devEnvironmentLabel)
        # Keys in data response are token_type (bearer) and access_token (your access token)
        accessToken = authResponse.json()['access_token']
        # Set Header: Authorization
        searchHeaders = { 'Authorization': 'Bearer {}'.format(accessToken) }
        # Set Param: query, fromData, toData, maxResults
        searchParams = { 'query': query,                # Query of the words you want to find
                          'fromDate': fromDate,         # First Date to Search (YYYYmmddHHMM)
                          'toDate': toDate,             # Last Date to Search (YYYYmmddHHMM)
                          'maxResults' : maxResults }   # Tweets Per Response (10~500, Sandbox(~100), Premium(~500))
        # GET Transmission Method(URL, header, param)
        searchResponse = requests.get(searchUrl, headers = searchHeaders, params = searchParams)
        # result list
        tweets = []
        # Add a line(tweet) to 'tweets'(result list)
        for tweet in searchResponse.json()['results']:
            tweets.append(tweet)
        # tweets(result list) return
        return tweets
    # ----------------------------------------------------------------------------------------------
    #  Get Search Timeline(Return Type: 'User' object)
    # ----------------------------------------------------------------------------------------------
    def searchTimeline(self, authResponse, screenName, count, include_rts):
        # Set URL
        searchUrl = '{}1.1/statuses/user_timeline.json'.format(self.baseUrl)
        # Keys in data response are token_type (bearer) and access_token (your access token)
        accessToken = authResponse.json()['access_token']
        # Set Header: Authorization
        searchHeaders = { 'Authorization': 'Bearer {}'.format(accessToken) }
        # Set Param: screenName, count
        searchParams = { 'screen_name': screenName,
                         'count': count,
                         'include_rts': include_rts}
        # GET Transmission Method(URL, header, param)
        searchResponse = requests.get(searchUrl, headers = searchHeaders, params = searchParams)
        # return object
        timeline = searchResponse.json()
        # 'User' object return
        return timeline
    # ----------------------------------------------------------------------------------------------
    #  Preproceeing
    # ----------------------------------------------------------------------------------------------
    def preprocess(self, tweets, json = [], hashtag = [], user = [], keyNum = 1):
        #Load Tweets One Line
        for t in tweets:
            # Table(TWEET_JSON)
            json.append(['-'.join([t['created_at'][26:30],      # Creation Date and Time (YYYY-mm-dd HH:MM:SS)
                                   self.mapMonth[t['created_at'][4:7]],
                                   t['created_at'][8:19]]),
                        t['id_str'],                            # str(id)
                        t['text'],                              # tweet
                        t['truncated'],                         #  
                        str(keyNum).zfill(4),                   # TWEET_HASHTAG(F.K)
                        str(keyNum).zfill(4),                   # TWEET_USER(F.K)
                        t['retweet_count'],                     # Retweet Count
                        t['favorite_count'],                    # Favorite Count
                        t['lang']])                             # Written Language
            # Table(TWEET_HASHTAG)
            for h in t['entities']['hashtags']:
                hashtag.append([str(keyNum).zfill(4),   # P.K
                               h['indices'][0],         # Start Position of Hashtag
                               h['indices'][1],         # End Position of Hashtag
                               h['text']])              # Hashtag
            # Table(TWEET_USER)
            user.append([str(keyNum).zfill(4),          # P.K
                         t['user']['id_str'],           # str(id)
                         t['user']['name'],             # User Name
                         t['user']['screen_name'],      # User Screen Name(@)
                         t['user']['location'],         # User Location
                         t['user']['description']])     # User Description
            # Increase in Key Value
            keyNum += 1
        # (json, hashtag, user) return
        return json, hashtag, user
# --------------------------------------------------------------------------------------------------
