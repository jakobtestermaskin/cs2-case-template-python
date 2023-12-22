import json


def handler(event, context):
    print(event)

    records = event['Records']
    body = json.loads(records['body'])

    print(body)
