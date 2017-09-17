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
	
searchKeywords = []
searchKeywords.append("rescue")
searchKeywords.append("help")
searchKeywords.append("save")
searchKeywords.append("flood")
searchKeywords.append("water")
searchKeywords.append("storm")
searchKeywords.append("rain")
searchKeywords.append("boat")
searchKeywords.append("harvey")
searchKeywords.append("houston")
print(searchKeywords)

query = ''
for keyword in searchKeywords:
	query = query + keyword + " "
	
print(query)

search_results = api.search(q="rescue OR help OR save OR flood OR water OR storm", count=numResults)
#startDate = datetime.datetime(2017, 8, 26, 0, 0, 0)
#endDate = datetime.datetime(2017, 8, 26, 23, 59, 59)

for tweet in search_results:
	print(tweet)