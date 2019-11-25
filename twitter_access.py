from __future__ import absolute_import, print_function

from tweepy import OAuthHandler, Stream, StreamListener

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="ynas81LQTRo2mAZn67AIHe3xF "
consumer_secret="ImpwBMWSWXEvftPCckj946nzmWW5TBL3RA3h5LiWSM6IsjN4Lm"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1196516799015206913-58KLah79srkiJw8dm1NzAAMct021wu"
access_token_secret="SHUm6iG11SucYpZic7jGt3HtzYkGDAxjDD0c58VRkV1qH"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])