from datetime import timedelta

from dateutil import parser

from discord import Discord
from twitter import Twitter


class DiscoTweets(Discord, Twitter):
    def __init__(self) -> None:
        super().__init__()

    def create_template_message(self, items: list) -> str:
        """
        create the messaeg as per the requrirement.
        argument:
            items: list of dictionary items
        return:
            template: the message in template given
        """
        try:
            template = "This week in team.shiksha:\n\n{}"
            string = ""
            for index, value in enumerate(items):
                event_name = value.get("event_name", "")
                event_schedule = value.get("event_schedule", "")
                if event_name and event_schedule:
                    date_time = parser.parse(event_schedule) + timedelta(hours=5.0, minutes=30.0)
                    date_time = date_time.strftime("%A, %d %b at %I:%M %p")
                    line_data = f"{index+1}. " + event_name + " on " + date_time + "\n"
                    string = string + line_data
            template = template.format(string)
        except Exception as template_err:
            raise template_err
        return template

    def runner(self):
        """
        runs the whole flow of the code
        """
        try:
            items = self.get_events()
            if items:
                template_message = self.create_template_message(items)
                if template_message:
                    self.post_events(template_message)
                    self.send_tweet(template_message)
        except Exception as runner_err:
            raise runner_err


if __name__ == "__main__":
    DiscoTweets = DiscoTweets()
    DiscoTweets.runner()
