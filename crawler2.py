import tweepy
import datetime
from tweepy import OAuthHandler
 
CONSUMER_KEY = '0dLatcH45xBzZnXpy0i0jbQ13'
CONSUMER_SECRET = 'wcbYlbz8dl0bM7bqn58nAEOkA4iN0W2SuGQpm30tMkLBU0zaQk'
ACCESS_TOKEN = '3162735390-IgHEWb8wUBumRLpY8CdZ2VA4V4LycTYBrkWtc04'
ACCESS_TOKEN_SECRET = '6fFWieYb8Kl7JnQK1jJtKdRlRGiqZUCU1Un8OVk2qkAUp'
 
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
 
api = tweepy.API(auth)

numResults = 0
while(numResults <= 0):
	print("Enter the max number of tweets to return: ")
	numResults = int(raw_input())
	
for tweet in tweepy.Cursor(api.search, q="#harvey (help OR rescue) boat", since="2017-08-26").items(numResults):
  print tweet.created_at, tweet.user.name, "(", tweet.user.screen_name, ")" , tweet.text

#search_results = api.search(q="#harvey (help OR rescue) boat", count=numResults)

#for tweet in search_results:
#	print(tweet)
