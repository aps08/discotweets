import os
from datetime import datetime, timedelta, timezone

import tweepy


class Twitter:
    """
    Responsible for sending the tweet message to twitter.
    """

    def send_tweet(self, tweet_message: str) -> None:
        """
        Iterate list items and converts
        them into tweet.
        argument:
            tweet_message: text message for the tweet.
        """
        try:
            client = tweepy.Client(
                bearer_token=os.environ.get("BEARER_TOKEN"),
                consumer_key=os.environ.get("API_KEY"),
                consumer_secret=os.environ.get("API_SECRET"),
                access_token=os.environ.get("ACCESS_TOKEN"),
                access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET"),
            )
            res = client.create_tweet(text=tweet_message)
        except Exception as send_tweet_err:
            raise send_tweet_err
