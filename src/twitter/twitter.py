import os
from datetime import datetime, timedelta, timezone

import tweepy
from tweepy.api import API
from tweepy.client import Client


class Creator:
    """
    Creates required objects for twitter API calls.
    """

    def get_client(self) -> Client:
        """
        Public function to create and return Client object.
        return:
            client: twitter client object.
        """
        try:
            client = tweepy.Client(
                bearer_token=os.environ.get("BEARER_TOKEN"),
                consumer_key=os.environ.get("API_KEY"),
                consumer_secret=os.environ.get("API_SECRET"),
                access_token=os.environ.get("ACCESS_TOKEN"),
                access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET"),
            )
        except Exception as client_obj_err:
            raise client_obj_err
        return client

    def get_oauth(self) -> API:
        """
        Public function to create and return OAuth object.
        return:
            auth: twitter OAuth object.
        """
        try:
            auth = tweepy.OAuthHandler(
                consumer_key=os.environ.get("API_KEY"),
                consumer_secret=os.environ.get("API_SECRET"),
                access_token=os.environ.get("ACCESS_TOKEN"),
                access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET"),
            )
            twitter_api = tweepy.API(auth)
        except Exception as oauth_obj_err:
            raise oauth_obj_err
        return twitter_api


class Twitter(Creator):
    def __init__(self) -> None:
        Creator.__init__(self)
        self.__client = self.get_client()
        self.__oauth_api = self.get_oauth()

    def send_tweet(self, items: list) -> None:
        """
        Iterate list items and converts
        them into tweet.
        argument:
            items:  list of dictionaries, where each
            dictionary contain message and image key.
        """
        try:
            for item in items:
                pass
        except Exception as send_tweet_err:
            raise send_tweet_err
