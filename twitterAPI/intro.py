import tweepy


API_KEY = "O0CSNkR9Dz5oLyOdzzuvwdQjP"
API_KEY_SECRET = "FgPDmbLGzIrHM10gWp6iQwuvfv6aNZvIZP3WQwmvG8xN6ZnIWm"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADZrawEAAAAAhIKxuzVkmGNKrlXvEcshMDAFwHc%3DSh7RIjngWP4WII6PJCE8bCJYNGS9xHnhiSdxZ2ISr1fcP7x4AY"

ACCESS_TOKEN = "1508342222336536576-ey4gF7WTTKhbWjSD1d671r7IOitHeE"
ACCESS_TOKEN_SECRET = "ibWHGiZUwC35ZmaBpUZznSCwBJ7UOhiBe8DoYletkaEFN"





client = tweepy.Client(bearer_token=BEARER_TOKEN)

query = 'from:nntaleb -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)


