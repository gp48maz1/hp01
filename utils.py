from wit import Wit

access_token = "6WI5F3AWG37B7SMUPI53VIKY4WSF3C4U"
access_token_dudley = "P2KLAZVQTTCKRFADW4WZ4JTELKT2FX4O"

client = Wit(access_token=access_token)
client_dudley = Wit(access_token=access_token_dudley)


def wit_response(message_text):
    resp = client.message(message_text)
    entity = None
    value = None

    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']
    except:
        pass
    return(entity, value)


def wit_dudley_response(message_text):
    resp = client_dudley.message(message_text)
    entity = None
    value = None

    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']
    except:
        pass
    return(entity, value)

#print(wit_response("I want to be in Ravenclaw"))