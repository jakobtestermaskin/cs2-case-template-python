try:
    import boto3
except:
    pass

try:
    from config import config
except:
    config = {"groupNumber": "g00"}

import datetime
import json
import os

import uuid


class PublisherClient:
    def publish_hint(self, id: str, text: str):
        sns = boto3.client("sns")

        topic_arn = os.environ.get("RESULTS_TOPIC_ARN")

        result = sns.publish(
            TopicArn=topic_arn,
            Message=json.dumps(
                {
                    "type": "hint",
                    "id": id,
                    "text": text,
                    "groupNumber": config["groupNumber"],
                }
            ),
            MessageStructure="string",
        )

        print("Published hint")

    def _song_publishment(self, type: str, song_name: str):
        id = str(uuid.uuid4())

        sns = boto3.client("sns")

        topic_arn = os.environ.get("RESULTS_TOPIC_ARN")
        print(topic_arn)

        message = json.dumps(
            {
                "type": type,
                "song_name": song_name,
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "groupNumber": config["groupNumber"],
                "id": id,
            }
        )

        result = sns.publish(
            TopicArn=topic_arn,
            Message=message,
            MessageStructure="string",
        )

        print("Published song event")

    def publish_song_started(self, song_name: str):
        self._song_publishment("song_started", song_name)

    def publish_song_ended(self, song_name: str):
        self._song_publishment("song_ended", song_name)


class PublisherClientMock:
    def publish_hint(self, id: str, text: str):
        print(f"Publishing {id} with text {text}")

    def publish_song_started(self, song_name: str):
        print(f"Song {song_name} started at {datetime.datetime.utcnow().isoformat()}")

    def publish_song_ended(self, song_name: str):
        print(f"Song {song_name} ended at {datetime.datetime.utcnow().isoformat()}")


class Publisher:
    def __init__(self, client):
        self.client = client

    def publish_song_started(self, song_name):
        self.client.publish_song_started(song_name)

    def publish_song_ended(self, song_name):
        self.client.publish_song_ended(song_name)

    def publish_hint(self, id: str, text: str):
        self.client.publish_hint(id, text)
