import tweepy
import datetime
from tweepy import OAuthHandler
from math import *

CONSUMER_KEY = '0dLatcH45xBzZnXpy0i0jbQ13'
CONSUMER_SECRET = 'wcbYlbz8dl0bM7bqn58nAEOkA4iN0W2SuGQpm30tMkLBU0zaQk'
ACCESS_TOKEN = '3162735390-IgHEWb8wUBumRLpY8CdZ2VA4V4LycTYBrkWtc04'
ACCESS_TOKEN_SECRET = '6fFWieYb8Kl7JnQK1jJtKdRlRGiqZUCU1Un8OVk2qkAUp'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

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

numResults = 0
while(numResults <= 0):
	print("Enter the max number of tweets to return: ")
	numResults = int(raw_input())

k = 0
while(k <= 0):
	print("Enter a value for k to find the k nearest neighbors: ")
	k = int(raw_input())

def jaccard(x, y):
	intersectionSize = len(set.intersection(*[set(x), set(y)]))
	unionSize = len(set.union(*[set(x), set(y)]))
	return intersectionSize/float(unionSize)

search_results = api.search(q="#harvey (help OR rescue) boat", count=numResults)

distances = []
for tweet in search_results:
	tweetWords = tweet.text.encode('utf-8').split()
#	print(tweet.text.encode('utf-8'))
	print(tweetWords)
	print(jaccard(searchKeywords, tweetWords))
	distances.append(jaccard(searchKeywords, tweetWords))

print(distances)
dist = 0.0
index = -1
KNN = []
for x in range(k):
	for d in range(len(distances)):
		if(distances[d] > dist):
			dist = distances[d]
			index = d
#	print index
	KNN.append(search_results[index])
#	print(dist)
	del distances[index]
	del search_results[index]
#	print(distances)
	index = -1
	dist = 0.0

for t in KNN:
	print(t.text.encode('utf-8'))
