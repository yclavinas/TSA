from TwitterSearch import *
import unicodedata
# import re
import datetime

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.setKeywords(['Tsukuba', 'tsukuba']) # let's define all words we would like to have a look for
    tso.setLanguage('en') # we want to see German tweets only
    tso.setCount(100) # please dear Mr Twitter, only give us 100 results per page
    tso.setIncludeEntities(False) # and don't give us all those entity information
    
    ####
    # Create the consumer_key, consumer_secret, access_token, acess_token_secret at https://apps.twitter.com/app/new
    # Add the info here
    ####
    ts = TwitterSearch(
		consumer_key = ,
		consumer_secret = ,
		access_token = ,
		access_token_secret = 
	)


    for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
        print( 'at %s' %   tweet['created_at'], tweet['text'])


    	date = tweet['created_at']
    	info = tweet['text']# + " " + date
    	data2Save = unicodedata.normalize('NFKD', info).encode('utf-8','ignore')

        saveFile = open('TsukubaShi.txt', 'a')
        saveFile.write(data2Save)
        saveFile.write('\n')
        saveFile.close()


except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)