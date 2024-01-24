import json
import urllib3
import sys

import config


try:
    arg = sys.argv[1]
except:
    arg = None


def get_events(groupNumber):
    http = urllib3.PoolManager()
    response = http.request(
        "GET",
        f"{config.get('logsFunctionUrl')}/{groupNumber}/events",
        headers={"Authorization": f"Bearer {config.get('accessToken')}"},
    )
    events = response.data.decode("utf-8")

    return json.loads(events)


def pretty_print_events(events, type):
    for event in events["events"]:
        if event["type"] == type:
            print(event["data"])


if __name__ == "__main__":
    pretty_print_events(get_events("g00"), arg)
