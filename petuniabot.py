import os
import time
from slackclient import SlackClient
from utils import wit_response

# starterbot's ID as an environment variable
BOT_ID_PETUNIA = os.environ.get("BOT_ID_PETUNIA")
BOT_ID_DUDLEY = os.environ.get("BOT_ID_DUDLEY")
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID_PETUNIA + ">"
AT_DUDLEY = "<@" + BOT_ID_DUDLEY + ">"
AT_HP = "<@" + BOT_ID + ">"

# rails
EXAMPLE_COMMAND = "do"
START_COMMAND = "bot exec"
RESPONSE_1 = "mom stop it I'm watching the tele!"
RESPONSE_2 = "fine... mother... but only because harry is scheduling it!"


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "EXECUSE ME!! You UNGRATEFUL little BRAT! Use proper English " \
               "when talking to me!"

    if command.startswith(AT_BOT):
        general_text = command.split(AT_BOT)[1].strip().lower()

        #response += START_COMMAND
        if general_text == START_COMMAND:
            response = AT_DUDLEY + "Dudders when was the last time you received a hair cut?"

        if general_text == RESPONSE_1:
            response = AT_DUDLEY + "Oh sweetums, I know you don't want to go, but we'll get Harry to " \
                       "schedule it."

        if general_text == RESPONSE_2:
            response = AT_HP + "Well BOY! Didn't you hear my sweetums. Get on with it!"
    '''''
    if command.startswith(EXAMPLE_COMMAND):

        response = None

        entity, value = wit_response(command)

        if entity == 'class_type':
            response = "Oh I love {}!".format(str(value))
        elif entity == 'house_type':
            response = "Oh {}, I love them!".format(str(value))

        if entity is None:
            response = "Stop being a muggle"

        words = command.split()
        for word in words:
            check = word
            if word == 'cool':
                response ="Niceeeeee"
            elif word == 'hogwarts':
                response = "I went there!"
            elif word == 'hermoine':
                response = "That is my best friend! Maybe even more than my best friend..."

        response = entity + value
    '''''

    slack_client_petunia.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                # return output['text'].split(AT_BOT)[1].strip().lower(),
                return output['text'], \
                       output['channel']
    return None, None


# instantiate Slack & Twilio clients
slack_client_petunia = SlackClient(os.environ.get('SLACK_BOT_TOKEN_PETUNIA'))

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client_petunia.rtm_connect():
        print("Aunt Petunia Bot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client_petunia.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")