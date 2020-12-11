import random, schedule, time

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

GOOD_MORNING = [
    "Good Morning Love!",
    "Good Morning Lovely!",
    "Hope you have a great day today",
    "Love you, I know you will slay the day"
]

GOOD_EVENING = [
    "Good Evening Love",
    "Sleep Tight My Love!",
    "Love you!"
]


def send_message(quotes_list=GOOD_MORNING):

    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote
                           )


# send a message in the morning
schedule.every().day.at("07:58").do(send_message, GOOD_MORNING)

# testing
schedule.every().day.at("13:55").do(send_message, GOOD_EVENING)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)
