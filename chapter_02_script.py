import os
from slackclient import SlackClient

#Grab Slack References from Environment
BOT_ID_PETUNIA = os.environ.get('BOT_ID_PETUNIA')
BOT_ID_DUDLEY = os.environ.get('BOT_ID_DUDLEY')
BOT_ID_HAGRID = os.environ.get('BOT_ID_HAGRID')
BOT_ID_HOGFORD = os.environ.get('BOT_ID_HOGFORD')
BOT_ID_BOB_HAIR_CUT = os.environ.get('BOT_ID_BOB_HAIR_CUT')


#Bot References within Slack
AT_PETUNIA = "<@" + BOT_ID_PETUNIA + ">"
AT_DUDLEY = "<@" + BOT_ID_DUDLEY + ">"
AT_HAGRID = "<@" + BOT_ID_HAGRID + ">"
AT_HOGFORD = "<@" + BOT_ID_HOGFORD + ">"
AT_BOB_HAIR_CUT = "<@" + BOT_ID_BOB_HAIR_CUT + ">"


#Script
START_COMMAND  = "hagrid exec"
CH02_hagrid_STATEMENT_01 = "Hello my name is RUUUU Hagrid, Keeper of Grounds and Green Energy at Hogford."
