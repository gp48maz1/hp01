import os
import time
from slackclient import SlackClient
from utils import wit_response, wit_dudley_response

# starterbot's ID as an environment variable
BOT_ID_PETUNIA = 'U7JK660E6'
BOT_ID_DUDLEY = os.environ.get("BOT_ID_DUDLEY")
BOT_ID = 'U7HQ4QJR2'

# constants
AT_BOT = "<@" + BOT_ID_DUDLEY + ">"
AT_HP = "<@" + BOT_ID + ">"
AT_PETUNIA = "<@" + BOT_ID_PETUNIA + ">"

# rails
EXAMPLE_COMMAND = "do"
QUESTION_1 = "dudders when was the last time you received a hair cut?"
QUESTION_2 = "oh sweetums, i know you don't want to go, but we'll get harry to " \
             "schedule it."


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "BOOOO Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."

    ##### NEEED TO FIX THE TRUE FALSE TAGS BAD STRUCTURE###
    if command.startswith(AT_BOT):
        check = False
        general_text = command.split(AT_BOT)[1].strip().lower()

        if general_text == QUESTION_1:
            response = AT_PETUNIA + "Mom stop it I'm watching the Tele!"
            check = True

        if general_text == QUESTION_2:
            response = AT_PETUNIA + "Fine... Mother... but only because Harry is scheduling it!"
            check = True

        ##########
        # WIT.AI #
        ##########
        if not check:

            entity, value = wit_dudley_response(command)

            response = "WOO" + entity + " " + value

            if entity == 'intent' and value == 'insult':
                response = "Shut Up Potter, you are a {}!".format(str(value))
            elif entity == 'intent' and value == 'threaten_with_magic':
                response = AT_PETUNIA + "Are you talking about magic?! Mummy! Mummy! Harry is " \
                                        "talking about {}!".format(str(value))
            #Can remove this dupe when i have dictionaries
            elif entity == 'object_attacking_with':
                response = AT_PETUNIA + "Are you talking about magic?! Mummy! Mummy! Harry is " \
                                        "talking about {}!".format(str(value))
            elif entity == 'object_of_insult':
                response = "Shut Up Potter, you are a {}!".format(str(value))

            if entity is None:
                response = "Harry you are A BIG STUPID IDIOT!!!!"

        '''''
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

    slack_client_dudley.api_call("chat.postMessage", channel=channel,
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
slack_client_dudley = SlackClient(os.environ.get('SLACK_BOT_TOKEN_DUDLEY'))

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client_dudley.rtm_connect():
        print("Dudley Bot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client_dudley.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")