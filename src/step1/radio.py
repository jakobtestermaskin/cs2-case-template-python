from publish import Publisher
from db.keyValueStore import KeyValueStore


def handle(events, store: KeyValueStore, publisher: Publisher):
    # Lag funksjonalitet her!
    print("Hello, ST24!")
    pass
