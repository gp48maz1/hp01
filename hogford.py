import os
import time
from slackclient import SlackClient
from utils import wit_response, wit_dudley_response

# starterbot's ID as an environment variable
BOT_ID_PETUNIA = 'U7JK660E6'
BOT_ID_DUDLEY = 'U7JL8RLEQ'
BOT_ID = 'U7HQ4QJR2'
BOT_HOGFORD = ''

# constants
AT_HOGFORD = "<@" + BOT_HOGFORD + ">"
AT_DUDLEY = "<@" + BOT_ID_DUDLEY + ">"
AT_HP = "<@" + BOT_ID + ">"
AT_PETUNIA = "<@" + BOT_ID_PETUNIA + ">"

# rails
START_COMMAND = "dudders when was the last time you received a hair cut?"


#random
READ_DELAY = 2

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "I am a Hogwarts text messaging service. I have very limited functionality because the muggle who developed" \
               " my programming is very, very lazy."

    ##### NEEED TO FIX THE TRUE FALSE TAGS BAD STRUCTURE###
    if command.startswith(AT_HOGFORD):
        check = False
        general_text = command.split(AT_HOGFORD)[1].strip().lower()

        if general_text == START_COMMAND:
            # @DOBY This response should execute once the user has scheduled the haircut
            # It should be a seemless transition. Once Bob says the haircut is set, the user should receive a message
            # from Hogford
            response = "Message from Hogford School of Science & Engineering. INCOMING STUDENT your email account has " \
                       "not yet been verified. Please log in and finish regirstration. All INCOMING STUDENTS must " \
                       "finish registration by September 1st. Text HELP for further assitance."

            time.sleep(READ_DELAY)
            check = True

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