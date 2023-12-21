
try:
    import boto3
except:
    pass

import datetime
import json
import os


def publish_hint(id: str, text: str):

    sns = boto3.client("sns")

    topic_arn = os.environ.get("RESULTS_TOPIC_ARN")

    result = sns.publish(
        TopicArn=topic_arn, Message=json.dumps({"type": "hint", "id": id, "text": text}), MessageStructure="string",
    )


def publish_hint_mock(id: str, text: str):
    print(f"Publishing {id} with text {text}")


def _song_publishment(type: str, song_name: str):

    sns = boto3.client("sns")

    topic_arn = os.environ.get("RESULTS_TOPIC_ARN")
    print(topic_arn)

    result = sns.publish(
        TopicArn=topic_arn, Message=json.dumps({"type": type, "song_name": song_name, "timestamp": datetime.datetime.utcnow().isoformat()}), MessageStructure="string",
    )


def publish_song_started(song_name: str):
    _song_publishment("song_started", song_name)


def publish_song_started_mock(song_name: str):
    print(f"Song {song_name} started at {datetime.datetime.utcnow().isoformat()}")


def publish_song_ended(song_name: str):
    _song_publishment("song_ended", song_name)


def publish_song_ended_mock(song_name: str):
    print(f"Song {song_name} ended at {datetime.datetime.utcnow().isoformat()}")
