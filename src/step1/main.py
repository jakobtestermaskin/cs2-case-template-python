"""
Ikke gjør endringer her
"""

from radio import handle

import json

from publish import publish_hint


def handler(event, context):

    print(event)

    # print("Handler was ran for g00")

    # records = event['Records']

    # radio_messages = [x['Sns']['Message'] for x in event['Records']]

    # print(radio_messages)

    # events_from_radio_messages = [json.loads(x)['events']
    #                               for x in radio_messages]

    # flattened_events = [
    #     item for row in events_from_radio_messages for item in row]

    # handle(flattened_events, publish_client=publish_hint)

    # return {"statusCode": 200}
