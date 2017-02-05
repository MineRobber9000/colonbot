import re
TWEET_RE=re.compile(".*hug.*colon.*")

def check(text):
	return TWEET_RE.match(text) != None
