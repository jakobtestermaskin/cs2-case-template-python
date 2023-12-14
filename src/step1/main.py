"""
Ikke gjør endringer her
"""
import json


def handler(event, context):
    print("Handler was ran for g00")

    records = event['Records']

    radio_messages = [x['Sns']['Message'] for x in event['Records']]

    events_from_radio_messages = [x['events']
                                  for x in json.loads(radio_messages)]

    print(events_from_radio_messages)

    return {"statusCode": 200}
