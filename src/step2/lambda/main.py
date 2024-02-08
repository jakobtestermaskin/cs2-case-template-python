"""
Ikke gjør endringer her
"""

import json
from payment_service import handle
from payment.adapter import PaymentAdapter, PaymentAdapterImpl


def handler(event, context):
    print(f"event: {event}")

    for record in event["Records"]:
        body = json.loads(record["body"])
        song = body.get("song", "drivers license")
        artist = body.get("artist", "olivia rodrigo")

        handle({"song": song, "artist": artist})


if __name__ == "__main__":
    handler(
        {
            "Records": [
                {
                    "body": '{"song": "1 step forward 3 steps backwards","artist": "oliva rodrigo"}'
                }
            ],
        },
        paymentAdapter=PaymentAdapter(PaymentAdapterImpl()),
    )
