from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import csv
import sys
import tweepy
import json
import string
import codecs


ckey = 'Qv1W3VAIGLiKgLUzUxcpbBUZt'
csecret = 'KnwLtnMEHqreKurJrraZzDR7W7YFPMfKorGGLelAKPoEgaG4qa'
atoken ='2164383906-fOfku3aU9JTzNU0kZz2JCIOLED0RDgmz06shkAG'
asecret ='kXuRKb4gqVqazYMFyO2Wr5XITadmbB60XpfUX8ek5cXv4'

class listener(StreamListener):
    
    def on_data(self,data):
        
     try:
      
        all_data = json.loads(data)
        id1 = all_data["id"]
        sname = unicode(all_data["user"]["name"])
        tweet = unicode(all_data["text"])
        followers = unicode(all_data["user"]["followers_count"])
        friends = unicode(all_data["user"]["friends_count"])
        status = unicode(all_data["user"]["statuses_count"])
        #retweet = str(all_data["user"]["retweet_count"])
        #entities = all_data["entities"]["hashtags"]
        hashtags = unicode(all_data ["entities"]["hashtags"])
        urls = unicode(all_data ["entities"]["urls"])
        
        if int(followers)!=0:
         reputation = unicode((int(friends) / int(followers)))
        else :
         reputation= u"0"
         
        NoOfWords=unicode( len(tweet.split()))
        
        NoOfChars = unicode(len(tweet) - tweet.count(" "))
        
        NoOfUrls = unicode(len(urls.split()))

        def counthashtags(lists):
         subs='#'
         global total
         total = 0
         MYlist = string.split(lists)
         for item in MYlist:
           if item.startswith(subs)== True:
            total += 1
         return total
        
        def count_input_character (input_str, character):
         return sum(w.startswith(character) for w in input_str.lower().split())
        
        NoOfTags=unicode( count_input_character (tweet, '#'))

        NoOfURLS1 = count_input_character (tweet,'https:')
        NoOfURLS2 = count_input_character (tweet,'www.')
        
        NoOfURLS = unicode(NoOfURLS1 + NoOfURLS2)
        
        print id1
        print sname
        print tweet
        #print entities
        print followers
        print friends
        #print status
        #print retweet
        #print hashtags
        #print urls
        print reputation
        print NoOfWords
        print NoOfChars
        print NoOfTags
        print NoOfURLS

        #followers,friends,status,retweet,entities 
        #print  data.text,data.created_at,data.followers_count, data.friends_count, data.favourites_count, data.statuses_count,data.retweet_count,data.entities

        
        saveThis =(str(id1) + '::' + unicode(sname) + '::' + str(tweet) + '::' + str(followers) + '::' + str(friends) +'::' + str( reputation) + ':: ' + str(NoOfWords) + '::' + str(NoOfChars) + '::' + str(NoOfTags) + '::' + str(NoOfURLS))
        ##################################### CHANGE FILE NAME HERE ##########################################################
        saveFile = open('agri.csv','a')
        
        saveFile.write(unicode(saveThis))
        saveFile.write('\n')
        saveFile.close()
                          
        return True
     except BaseException, e:
        print 'failed ondata,',str(e)
        time.sleep(5)

    def on_error(self,status):
        print status

#auth = tweepy.OAuthHandler(ckey,csecret)
#auth.set_access_token(atoken,asecret)
#api = tweepy.API(auth)
#streamingAPI = tweepy.streaming.Stream(auth, StreamListener())
auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth, listener())
################# CHANGE TREND NAME HERE #####################################################################################
twitterStream.filter(track =["#Agriculture"])
twitterStream.filter(languages=["en"])

