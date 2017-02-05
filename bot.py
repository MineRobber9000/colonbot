import tweepy,checker
from time import sleep
from keys import *

responded_to = []

def log(action):
	with open("log.txt","ab") as f:
		f.write(action)

auth = tweepy.OAuthHandler(C_KEY,C_SECRET)
auth.set_access_token(A_KEY,A_SECRET)
api = tweepy.API(auth)

RESPONSE = "umm... you're hugging him wrong."

def runTime():
	# newest tweets from anyone
	newtweets = api.search(q="colon")
	# is it new?
	for tweet in newtweets:
		# have we already seen this tweet? if so, carry on past it
		if tweet.id in responded_to:
			continue
		# does it match what we're looking for?
		if checker.check(tweet.text):
			# reply in the form "@user <RESPONSE>"
			sn = tweet.user.screen_name
			m = "@{} {}".format(sn,RESPONSE)
			api.update_status(m,tweet.id)
			responded_to.append(tweet.id)
			log("Responded to @{}, who said \"{}\".".format(sn,tweet.text))

while True:
	runTime()
	sleep(15)
