Send a tweet with user inputs. The text body of the tweet, a link if desired, as well as an image file. If no link is to be added, hit Enter to skip that option. If for some reason your tweet is not sent, console prints the error message and restarts in continuos loop

Need to pip install tweepy

Create Twitter Developer Account (usually 1 or 2 day approval time)

Replace your Developer Account credentials here

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
