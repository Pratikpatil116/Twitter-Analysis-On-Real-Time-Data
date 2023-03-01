import tweepy
from textblob import TextBlob

consumer_key = "tfH5NYUhi6mln60JDYRuqjrKn"
consumer_secret ="ViD4tBKoqSs5KgTZBoRJIFvsieJ9SevTLQAWWwvvE5K5FJC7kr"

access_token ="1194914448793686018-jpzibdUZ7yJybMK75IgEyt90LOTXc1"
access_token_secret ="fvT8uV70okmdUcQ8SEGG4PE8jHTI3PMEui6jIxpvZWBtW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = tweepy.Cursor(api.search_tweets, q="Infosys", lang="en", result_type="recent").items(200)
count=0
for tweet in public_tweets:
     print(tweet.text)
     analysis = TextBlob(tweet.text)
     print(analysis.sentiment)
     count=count+1


print(count)
