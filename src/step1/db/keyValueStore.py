

class KeyValueStore:

    def __init__(self, client):
        self.client = client

    def get(self) -> dict:
        """
        Return the groups key value store
        """
        return self.client.get_key_value_store()

    def store(self, data: dict) -> dict:
        """
        Store dictionary that can be used again later. 
        Store any dict you want. 
        """
        return self.client.store_key_value_store(data)
