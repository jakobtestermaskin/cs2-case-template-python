

from publish import publish_hint_mock


def handle(events, publish_client=publish_hint_mock):

    for event in events:
        if (event['type'] == "hint"):
            publish_client(id=event['id'], text=event['text'])

    for i in range(1, len(events) - 1):
        current_event = events[i]

        print(current_event)

        if (events[i - 1]['song_name'] != current_event['song_name']):
            if (events[i-1]['song_name'] == None):
                print("started")

            elif current_event['song_name'] == None:
                print("ended")