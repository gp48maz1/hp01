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
#Block 0
CH02_hagrid_STATEMENT_01 = "S'rry for eh' not hav'in no eh proper intr'duct'in there earlier... " \
                           "My name is Rubeus Hagrid, Keeper o' Grounds an' Green Energy at Hogfor'. And I brought " \
                           "ya' here to Diagon Net so ya' could get yer' science supplies. Ya' know what yer need?"

#Block 1
CH02_hagrid_REPLY_01_Negative = "Ya I figur'd as much livin with the Dursleys 'n all. Well yer gotta get yer W.A.N.D.s " \
                                "(Wirelessly Activated Nano Device), you got yer digital currencies like BitKnuts an' " \
                                "er SickleCoin n' er ZGalleons... n' oh err you want me to keep goin? " \

CH02_hagrid_REPLY_01_Postive = "Oh yer do? Wel' er sorry for leavin' yer in the hotel room 'den. I was fittin to get it" \
                               " a fer " \
                               "yer anyway... I thoughts yer might not known nothin' 'bout no er surplies given ya " \
                               "know yer livin' with ther' Dursleys n' all. Well ter'day I wanted to grab yer BitKnuts, " \
                               "SickleCoin, n' ZGalleons from Gringots Venture Partners so we can pay fer yer W.A.N.D " \
                               "(Wirelessly Activated Nano" \
                               "Device). So do yer want to know anymore about what all is here in the Valley of Silicon?"

#Block 2
CH02_hagrid_REPLY_02_Negative = "OK well time to go off to Gringots Venture Partners, ready?"

CH02_hagrid_REPLY_02_Positive = "OK well yer got yer drone's for delivering packages n' such, the most popular brand " \
                                "there bein' Owl. Oh yer also got yer hoverboards for playin' Quidditch... Hmm what " \
                                "othe' items, oh ye, ya also got yer lab cloaks ther' important when tinkerin' n' " \
                                "such... Well I think thats about it fer now... If yer ready I'll go to Gringots" \
                                " Venture Partners, ready?"

#Block 3
CH02_hagrid_REPLY_03_Positive = "O' good to hear! Well I just got to Gringots Venture Partners, as they say \"Safest " \
                                "place in der whole worl' besides Hogfor'\". Oh that remin's me I need to pic up a " \
                                "certain secret littl' something for Professor Wozniak..."

#QUESTION about Prof Woz

#question about Woz
CH02_hagrid_REPLY_03_Woz = "Blimmey Potter, I forgot you know nothing about Hogfor' well Professor Marc " \
                                "Wozniak is the greates' engineer of them all! If I didn' know no better I woulda " \
                                "said he was er Wizard! Oh just finished up at Gringots, time to stop by Olivander's" \
                                " fer yer W.A.N.D... actually let me just send him an text, he can probably just send " \
                                "yer W.A.N.D. by Owl."

#When olivander finishes up

#Block 4
CH02_hagrid_REPLY_04_Ending = "Olivander just texted me yer all done pic'in' out yer W.A.N.D and perfect timeing! I" \
                              "just finished grabbing you a special somethin' -- a Snowy White Owl! It's a limited " \
                              "edition drone I got ya here 'ary. It's called Hedwig!"