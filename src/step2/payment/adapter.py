import os
import json
import datetime

try:
    import boto3
    import uuid
except:
    pass


class PaymentAdapterImpl:
    def pay(self, account_number, amount, artist):
        sns = boto3.client("sns")

        topic_arn = os.environ.get("PAYMENT_TOPIC_ARN")

        result = sns.publish(
            TopicArn=topic_arn,
            Message=json.dumps(
                {
                    "id": uuid.uuid4(),
                    "accountNumber": account_number,
                    "amount": amount,
                    "artist": artist,
                    "timestamp": datetime.datetime.utcnow().isoformat(),
                },
                default=str,
            ),
            MessageStructure="string",
        )

        print(result)

        print(f"Made payment: NOK {amount} to {account_number}")


class PaymentAdapterMock:
    def pay(self, account_number, amount, artist):
        print(f"Payment for ${artist} on ${amount} has been made to {account_number}")


class PaymentAdapter:
    def __init__(self, client):
        self._client = client

    def pay(self, account_number: str, amount: str, artist: str):
        self._client.pay(account_number, amount, artist)
