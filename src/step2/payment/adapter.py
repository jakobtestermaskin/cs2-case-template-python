import os
import json

try:
    import boto3
    import uuid
except:
    pass


class PaymentAdapterImpl:
    def pay(self, account_number, amount):
        sns = boto3.client("sns")

        topic_arn = os.environ.get("PAYMENT_TOPIC_ARN")

        result = sns.publish(
            TopicArn=topic_arn,
            Message=json.dumps(
                {
                    "id": uuid.uuid4(),
                    "accountNumber": account_number,
                    "amount": amount,
                }
            ),
            MessageStructure="string",
        )

        print(f"Made payment: NOK {amount * 100} to {account_number}")


class PaymentAdapterMock:
    def pay(self, account_number, amount):
        print(f"Payment ${amount} has been made to {account_number}")


class PaymentAdapter:
    def init(self, client):
        self.client = client

    def pay(self, account_number, amount):
        self.client.pay(account_number, amount)
