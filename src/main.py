import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_messages():
    token = os.environ.get("TOKEN")
    headers = {"authorization": f"Bot {token}"}
    response = requests.get("https://discord.com/api/v10/channels/1073307507172311122/messages", headers=headers)
    print(response, response.text)


get_messages()
