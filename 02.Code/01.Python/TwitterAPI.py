# --------------------------------------------------------------------------------------------------
# TwitterAPI.py
#      Title: Twitter Application Authentication, Collect Twitter Data, Data preprocessing
#     Author: Lee SeokJune
#  Create on: 2019.04.17
# --------------------------------------------------------------------------------------------------
# import module
## Python Module available on Twitter
import tweepy
# --------------------------------------------------------------------------------------------------
# Class Name: TwitterAPI
# Method list: OAuth
#            : searchKeyword, searchUser
#            : resultSearchResults, 
class TwitterAPI:
    # ----------------------------------------------------------------------------------------------
    # Twitter Application Authentication(Return Type: api)
    def OAuth(self, consumer_key, consumer_secret, access_token, access_token_secret):
        # Page located at http://dev.twitter.com/apps(under "OAuth settings")
        ## consumer_key, consumer_secret
        # Page located at http://dev.twitter.com/apps(under "Your access token")
        ## access_token, access_token_secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        # api return
        return api
    # ----------------------------------------------------------------------------------------------
    # Keyword in Tweet(Return Type: list)
    def searchKeyword(self, api, query, since, until, lang, limit):
        ## api: result of TwitterAPI.OAuth
        ## query: Words included in the Tweet you want to find(ex. KOREA OR JAPAN OR CHINA)
        ## since: Start Date
        ## until: End Date
        ## lang: The Language of the Tweets
        ## limit: Defines the maximum amount of Tweets to fetch
        # result list
        tweets = []
        try:
            # Return Type: list of 'SearchResults' objects
            for tweet in tweepy.Cursor(api.search, q = query, since = since, until = until, lang = lang, tweet_mode = 'extended').items(limit):
                # Add a line(tweet) to 'tweets'(result list)
                tweets.append(tweet)
            # tweets(result list) return
            return tweets
        # The main exception Tweepy uses. Is raised for a number of things.
        except tweepy.error.TweepError:
            print("Error(search_Keyword): Tweet Per Minute")
    # ----------------------------------------------------------------------------------------------
    # User in Twitter(Return Type: 'User' object)
    def searchUser(self, api, identificationInfo):
        ## api: result of TwitterAPI.OAuth
        ## identificationInfo: user_id OR screen_name
        ### user_id: Specifies the ID of the user. Helpful for disambiguating when a valid user ID is also a valid screen name.
        ### screen_name: Specifies the screen name of the user. Helpful for disambiguating when a valid screen name is also a user ID.
        try:
            # Return Type: 'User' object
            userInfo = api.get_user(identificationInfo)
            # userInfo('User' object) return
            return userInfo
        # The main exception Tweepy uses. Is raised for a number of things.
        except tweepy.error.TweepError:
            print("Error(search_User): Tweet Per Minute")
    # ----------------------------------------------------------------------------------------------
    # result Keyword
    def resultSearchResults(self, tweets):
        ## tweets: result of TwitterAPI.searchKeyword
        # result list(json, hashtag, metadata, user)
        json = []       # Table(SR_JSON)
        hashtag = []    # Table(SR_HASHTAG)
        metadata = []   # Table(SR_METADATA)
        user = []       # Table(SR_USER)
        # P.K('hashtag', 'metadata', 'user')
        keyNum = 1
        # ------------------------------------------------------------------------------------------
        # Load tweets One Line 
        for t in tweets:
            # --------------------------------------------------------------------------------------
            # '_json' Select
            json = t._json
            # --------------------------------------------------------------------------------------
            # Table(SR_JSON)
            keywordJson.append([json['created_at'],
                                json['id'],
                                json['id_str'],
                                json['text'],
                                json['truncated'],
                                str(keyNum).zfill(4),
                                str(keyNum).zfill(4),
                                json['source'],
                                json['in_reply_to_status_id'],
                                json['in_reply_to_status_id_str'],
                                json['in_reply_to_user_id'],
                                json['in_reply_to_user_id_str'],
                                json['in_reply_to_screen_name'],
                                str(keyNum).zfill(4),
                                json['geo'],
                                json['coordinates'],
                                json['place'],
                                json['contributors'],
                                json['is_quote_status'],
                                json['retweet_count'],
                                json['favorite_count'],
                                json['favorited'],
                                json['retweeted'],
                                #json['possibly_sensitive'],
                                json['lang']])
            # --------------------------------------------------------------------------------------
            # Table(SR_HASHTAGS)
            hashtags = json['entities']['hashtags']
            for h in hashtags:
                keywordHashtags.append([str(keyNum).zfill(4),
                                        h['text'],
                                        h['indices']])
            # --------------------------------------------------------------------------------------
            # Table(SR_METADATA)
            metadata = json['metadata']
            keywordMetadata.append([str(keyNum).zfill(4),
                                    metadata['iso_language_code'],
                                    metadata['result_type']])
            # --------------------------------------------------------------------------------------
            # Table(SR_USER)
            user = json['user']
            keywordUser.append([str(keyNum).zfill(4),
                                user['id'],
                                user['id_str'],
                                user['name'],
                                user['screen_name'],
                                user['location'],
                                user['description'],
                                user['url'],
                                user['protected'],
                                user['followers_count'],
                                user['friends_count'],
                                user['listed_count'],
                                user['created_at'],
                                user['favourites_count'],
                                user['utc_offset'],
                                user['time_zone'],
                                user['geo_enabled'],
                                user['verified'],
                                user['statuses_count'],
                                user['lang'],
                                user['contributors_enabled'],
                                user['is_translator'],
                                user['is_translation_enabled'],
                                user['following'],
                                user['follow_request_sent'],
                                user['notifications'],
                                user['translator_type']])
            # --------------------------------------------------------------------------------------
            # Increase in Key Value
            keyNum += 1
        # ------------------------------------------------------------------------------------------
        return keywordJson, keywordHashtags, keywordMetadata, keywordUser
    # ----------------------------------------------------------------------------------------------
    # result UserInfo
    def result_User(self, userInfo):
        userJson = [] # Table(User_JSON)
        # _json 선택 ------------------------------------------------------------------------------
        json = userInfo._json
        # Table(User_JSON) -----------------------------------------------------------------------
        userJson.append([json['id'],
                         json['id_str'],
                         json['name'],
                         json['screen_name'],
                         json['location'],
                         json['profile_location'],
                         json['description'],
                         json['url'],
                         json['protected'],
                         json['followers_count'],
                         json['friends_count'],
                         json['listed_count'],
                         json['created_at'],
                         json['favourites_count'],
                         json['utc_offset'],
                         json['time_zone'],
                         json['geo_enabled'],
                         json['verified'],
                         json['statuses_count'],
                         json['lang'],
                         json['contributors_enabled'],
                         json['is_translator'],
                         json['is_translation_enabled'],
                         json['profile_background_color'],
                         json['profile_background_image_url'],
                         json['profile_background_image_url_https'],
                         json['profile_background_tile'],
                         json['profile_image_url_https'],
                         #json['profile_banner_url'],
                         json['profile_link_color'],
                         json['profile_sidebar_border_color'],
                         json['profile_sidebar_fill_color'],
                         json['profile_text_color'],
                         json['profile_use_background_image'],
                         json['has_extended_profile'],
                         json['default_profile'],
                         json['default_profile_image'],
                         json['following'],
                         json['follow_request_sent'],
                         json['notifications'],
                         json['translator_type']])

        return userJson
