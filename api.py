from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#consumer key, consumer secret, access token, access secret.
ckey="xxxxxxxxxxxxxxxxxxxxxxxxxx" #write your own ckey
csecret="xxxxxxxxxxxxxxxxxxxxxxxxxxx"  #write your own csecret
atoken="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  #write your own atoken
asecret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  #write your own asecret

class listener(StreamListener):
    def on_data(self,data):
        all_data = json.loads(data)
        tweet =  all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print((tweet).translate(non_bmp_map), sentiment_value, confidence)

        if confidence*100 >=80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

twitterStream = Stream(auth,listener())
twitterStream.filter(track=["best"])
