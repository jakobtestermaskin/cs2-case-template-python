

from publish import Publisher
from db.keyValueStore import KeyValueStore


def handle(events, store: KeyValueStore, publisher: Publisher):

    print("Here you should handle the data")
