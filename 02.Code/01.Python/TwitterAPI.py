'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
TwitterAPI.py
      Title: TwitterAPI의 어플리케이션 인증, 데이터 수집(search,getuser), db저장 할 형식으로 변환
     Author: Lee SeokJune
  Create on: 2019.04.17 09:42
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import tweepy

class TwitterAPI:
    # Twitter Application 인증 -> api -------------------------------------------------------------
    def OAuth(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    # Keyword Search in Tweet --------------------------------------------------------------------
    def search_Keyword(self, api, keyword, sinceD, untilD, mode, count):
        tweets = []
        try:
            for tweet in tweepy.Cursor(api.search, q = keyword, since = sinceD, until = untilD, tweet_moede = mode,count = count).items():
                tweets.append(tweet)
            return tweets
        except tweepy.error.TweepError:
            print("Tweet Per Minute")
    # User Search --------------------------------------------------------------------------------
    def search_User(self, api, screen_name):
        userInfo = api.get_user(screen_name)
        return userInfo
    # result Keyword -----------------------------------------------------------------------------
    def result_Keyword(self, tweets):
        keywordJson = []        # Table(KEYWORD_JSON)
        keywordHashtags = []    # Table(KEYWORD_HASHTAGS)
        keywordMetadata = []    # Table(KEYWORD_METADATA)
        keywordUser = []        # Table(KEYWORD_J_USER)
        keyNum = 0
        # tweet 하나씩 가져오기 --------------------------------------------------------------------
        for t in tweets:
            # _json 선택 -------------------------------------------------------------------------
            json = t._json
            # Table(KEYWORD_JSON) ----------------------------------------------------------------
            keywordJson.append([json['created_at'],
                       json['id'],
                       json['id_str'],
                       json['text'],
                       json['truncated'],
                       str(keyNum + 1).zfill(4),
                       str(keyNum + 1).zfill(4),
                       json['source'],
                       json['in_reply_to_status_id'],
                       json['in_reply_to_status_id_str'],
                       json['in_reply_to_user_id'],
                       json['in_reply_to_user_id_str'],
                       json['in_reply_to_screen_name'],
                       str(keyNum + 1).zfill(4),
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
            # Table(KEYWORD_HASHTAGS) ------------------------------------------------------------
            hashtags = json['entities']['hashtags']
            for h in hashtags:
                keywordHashtags.append([str(keyNum + 1).zfill(4),
                                        h['text'],
                                        h['indices']])
            # Table(KEYWORD_METADATA) ------------------------------------------------------------
            metadata = json['metadata']
            keywordMetadata.append([str(keyNum + 1).zfill(4),
                                    metadata['iso_language_code'],
                                    metadata['result_type']])
            # Table(KEYWORD_USER) ----------------------------------------------------------------
            user = json['user']
            keywordUser.append([str(keyNum + 1).zfill(4),
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
            # key 증가 ----------------------------------------------------------------------------
            keyNum += 1
        return keywordJson, keywordHashtags, keywordMetadata, keywordUser
    # result UserInfo ----------------------------------------------------------------------------
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
