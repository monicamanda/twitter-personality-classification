import csv
import tweepy

# Get your Twitter API credentials and enter them here
apikeyData = open("apikey", "r").read().split(',')
consumer_key = apikeyData[0]
consumer_secret = apikeyData[1]
access_token = apikeyData[2]
access_token_secret = apikeyData[3]

# method to get a user's last tweets


def get_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # set count to however many tweets you want
    limit = 100

    # get tweets
    tweets_for_csv = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username).items(limit):
        # create array of tweet information: username, tweet id, date/time,
        # text
        tweets_for_csv.append(
            [username, tweet.created_at, tweet.text.encode("utf-8")])

    # write to a new csv file from the array of tweets
    outfile = "tweets-@" + username + ".csv"
    print("writing to ... " + outfile + " ... complete.")
    with open(outfile, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["username", "created_at", "text"])
        csvwriter.writerows(tweets_for_csv)


# if we're running this as a script
if __name__ == '__main__':
    # get tweets through multiple users
    users = ["_monicamanda", "quantavandal"]
    for user in users:
        get_tweets(user)
