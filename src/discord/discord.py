import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


class Discord:
    def __init__(self) -> None:
        self.__token = os.environ.get("TOKEN")
        self.__url = "https://discord.com/api/v10/"
        self.__headers = {"authorization": f"Bot {self.__token}"}

    def get_events(self) -> list:
        """
        Fetches event from discord server,
        and create a list of dictionary of important
        key items

        return:
            event_items: list of dictionary
        """
        try:
            event_items = []
            guild_id = os.environ.get("GUILD_ID")
            api_url = self.__url + "guilds/" + guild_id + "/scheduled-events"
            response = requests.get(api_url, headers=self.__headers)
            if response.ok:
                events = json.loads(response.text)
                for event in events:
                    event_name = event.get("name", "")
                    event_schedule = event.get("scheduled_start_time", "")
                    if event_schedule and event_name:
                        event_items.append({"event_name": event_name, "event_schedule": event_schedule})
                    else:
                        raise ValueError("event_name or event_schedule doesn't exists")
        except Exception as get_event_err:
            raise get_event_err
        return event_items

    def post_events(self, message: str) -> bool:
        """
        Post the events in the discord channel.
        argument:
            message: the content to be send on the discord
                    channel.
        return:
            sent: True is message was send successfully.
        """
        try:
            sent = False
            channel_id = os.environ.get("CHANNEL_ID")
            payload = {"content": message}
            api_url = self.__url + "channels/" + channel_id + "/messages"
            response = requests.post(api_url, data=payload, headers=self.__headers)
            if response.ok:
                sent = True
        except Exception as post_event_err:
            raise post_event_err
        return sent
