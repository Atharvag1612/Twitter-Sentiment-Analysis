

import tweepy
import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


#Configuring Twitter Keys for user account with developer access.
auth = tweepy.OAuthHandler("XOesClHbdlCiaIzZgCLpkXZEs", "bjQ13vvXeSvotG8YhWvMjjJ26XEpTAVu9UmjvLbMhng1QHAzDM")
auth.set_access_token("1597672903662706688-3jGsQ3jdWTwyftJv9r4w0uwQE1BMXC", "X4nk4VNWaGMYWAIOybiDpydysmkIOhhouebH5qLJH3ggV")

api = tweepy.API(auth,wait_on_rate_limit=True)

today = datetime.date.today()
yesterday= today - datetime.timedelta(days=10000)
today, yesterday
max_tweets=6000

analyzer = SentimentIntensityAnalyzer()


tweets_list = tweepy.Cursor(api.search_tweets, q="#UW OR #University of Washington OR #Huskies since:" + str(yesterday)+ " until:" + str(today),tweet_mode='extended', lang='en').items(max_tweets)

output_n=[]
output_p=[]
# Process tweets
for tweet in tweets_list:
    text = tweet.full_text
    score = analyzer.polarity_scores(text)
    if score['compound'] < 0:
        line_n = {'text' : text}
        output_n.append(line_n)
    elif score['compound'] > 0:
        line_p = {'text' : text}
        output_p.append(line_p)

df_n = pd.DataFrame(output_n)
df_n.to_json(r'C:\Users\Atharva\Documents\uw_n_negative.json')

df_p = pd.DataFrame(output_p)
df_p.to_json(r'C:\Users\Atharva\Documents\uw_n_positive.json')