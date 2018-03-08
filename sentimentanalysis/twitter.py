import tweepy
from textblob import TextBlob

consumer_key = 'oib7sbWhFrwzxghfqWWBqcQb5'
consumer_secret = 'dZI5WB8JI0cE5dHyxIo5YFhKqKcF6TWn2ZpwX43ATdT8q46gDv'

access_token = '565327581-xBeIFfCqFCTamzMiYscdcZFJl0aUlJJXsgaJK0VM'
access_token_secret = 'cMGOUiQqfS7hy7k8QltHG9lkKLeSIIycz5ehBnqM4twVV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
