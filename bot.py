import tweepy,checker
from keys import *

def log(action):
	with open("log.txt","ab") as f:
		f.write(action)

auth = tweepy.OAuthHandler(C_KEY,C_SECRET)
auth.set_access_token(A_KEY,A_SECRET)
api = tweepy.API(auth)

RESPONSE = "umm... you're hugging him wrong."

lasttweet = None

def runTime():
	# use global lasttweet
	global lasttweet
	# newest tweet from anyone
	newtweet = api.search(q="from:*")
	# is it new?
	if newtweet != lasttweet:
		# does it match what we're looking for?
		if checker.check(newtweet.text):
			# reply in the form "@user <RESPONSE>"
			sn = newtweet.user.screen_name
			m = "@{} {}".format(sn,RESPONSE)
			api.update_status(m,newtweet.id)
			log("Responded to @{}, who said \"{}\".".format(sn,newtweet.text))
	# save the new tweet as it is now the latest one we've processed.
	lasttweet = newtweet

while True:
	runTime()
	sleep(15)
