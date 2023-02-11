import json
import os
from datetime import timedelta

import requests
from dateutil import parser
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
            response = requests.get(self.__url + "guilds/" + guild_id + "/scheduled-events", headers=self.__headers)
            if response.ok:
                events = json.loads(response.text)
                for event in events:
                    event_name = event.get("name", "")
                    event_schedule = event.get("scheduled_start_time", "")
                    if event_schedule and event_name:
                        date_time = parser.parse(event_schedule) + timedelta(hours=5.0, minutes=30.0)
                        date_time = date_time.strftime("%A, %d %b at %I:%M %p")
                        event_items.append(event_name + " on " + date_time)
                    else:
                        raise ValueError("event_name or event_schedule doesn't exists")
            else:
                raise ValueError("API call failed")
        except Exception as get_event_err:
            raise get_event_err
        return event_items

    def post_events(self) -> None:
        """
        Post the events in the discord server for
        reminder.
        """
        try:
            channel_id = os.environ.get("CHANNEL_ID")
            pass
        except Exception as post_event_err:
            raise post_event_err


Discord = Discord()
string = ""
for index, item in enumerate(Discord.get_events()):
    string = string + f"{index+1}. {item}" + "\n"
print(string)
