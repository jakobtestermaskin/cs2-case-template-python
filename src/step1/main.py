"""
Ikke gjør endringer her
"""
import json


def handler(event, context):
    print("Handler was ran for g00")

    print(event)

    return {"statusCode": 200}
