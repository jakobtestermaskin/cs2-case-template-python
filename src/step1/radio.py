

from publish import publish_hint_mock, publish_song_started, publish_song_ended
from db.keyValueStore import KeyValueStore


def handle(events, store: KeyValueStore, publish_client=publish_hint_mock):

    key_value_store = store.get()

    for event in events:
        if (event['type'] == "hint"):
            pass
            # publish_client(id=event['id'], text=event['text'])

    last_seen_song = key_value_store.get("LAST_SEEN_SONG", None)

    for i in range(0, len(events)):

        current_event = events[i]

        # print(current_event)

        if (last_seen_song != current_event['song_name']):  # shift in song

            def start(name):
                publish_song_started(name)

            def end(name):
                publish_song_ended(name)

            # En sang begynner rett etter hint
            if (current_event['song_name'] and last_seen_song == None):
                start(current_event['song_name'])
            # sang ferdig, hint begynner
            elif (current_event['song_name'] == None and last_seen_song != None):
                end(last_seen_song)

            # Går rett fra en sang til en annen
            elif (current_event['song_name'] != None and last_seen_song != None and current_event['song_name'] != last_seen_song):
                end(last_seen_song)
                start(current_event['song_name'])

        last_seen_song = current_event['song_name']

    store.store({"LAST_SEEN_SONG": last_seen_song})
