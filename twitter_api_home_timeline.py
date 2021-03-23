# Derek Cross python code to show importing data from my Twitter API (Home timeline).
import tweepy

# Authenticate to Twitter - Setup security keys.
auth = tweepy.OAuthHandler("ZhsGFGA6twuzFT9ZH99K16E48",
    "aYwVl9eikRXYylcQB0xxp3FUz2oYTrY3xsGARmMkbr4GMJMhLP")
#tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token("1347989941024940032-wTj6f6tT34oL2slakxKvk6xFKUYLSg",
    "g35B5svvrVkzE1n6jmNwC7hrTsfuhAzA6EVmC4t2eDj48")
#auth.set_access_token(access_token,access_token_secret)

# Create API object
api = tweepy.API(auth)

# Print home timeline tweets text
public_tweets = api.home_timeline()
for tweet in public_tweets:
    #print out my twitter home timeline.
    print(tweet.text)
