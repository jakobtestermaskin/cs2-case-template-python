import json
from step2_handler import handle


def handler(event, context):

    song = event['body'].get("song", "drivers license")
    artist = event['body'].get("artist", "olivia rodrigo")

    handle({"song": song, "artist": artist})


if __name__ == '__main__':
    handler({"body": {"song": "1 step forward 3 steps backwards",
            "artist": "oliva rodrigo"}}, {})
