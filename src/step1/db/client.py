from abc import ABC, abstractmethod

import json
import os

try:
    import boto3
    from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
except:
    pass

table_name = os.environ.get("DYNAMO_DB_TABLE_NAME",
                            "Cs2-step1-key-value-store-g00",
                            )


class KeyValueStoreClient(ABC):
    @abstractmethod
    def get_key_value_store():
        pass

    @abstractmethod
    def store_key_value_store(data: dict):
        pass


class KeyValueStoreClientImpl(KeyValueStoreClient):

    def get_key_value_store(self):

        def dynamo_obj_to_python_obj(dynamo_obj: dict) -> dict:
            deserializer = TypeDeserializer()
            return {
                k: deserializer.deserialize(v)
                for k, v in dynamo_obj.items()
            }

        client = boto3.client("dynamodb")

        result = client.get_item(Key={
            "type": {
                "S": "key_value_store"

            }}, TableName=table_name)

        item = dynamo_obj_to_python_obj(result.get('Item', {}))

        if "type" in item:
            del item['type']

        return item.get("data", {})

    def store_key_value_store(self, data: dict):

        client = boto3.client("dynamodb")

        result = client.put_item(TableName=table_name, Item={
            "type": {
                "S": "key_value_store"
            },
            "data": TypeSerializer().serialize(data)
        })

        return data


key = "step1.json"
directory = ".storage"


def take(path):
    if (not os.path.exists(path)):
        os.makedirs(path)


def get_or_create_file(directory, key):
    take(directory)

    file_path = f"{directory}/{key}"

    if (not os.path.exists(file_path)):
        with open(file_path, "w") as f:
            f.write("{}")
        return {}

    else:
        with open(file_path, "r") as f:
            return json.load(f)


class KeyValueClientMock(KeyValueStoreClient):

    def get_key_value_store(self):
        return get_or_create_file(directory=directory, key=key)

    def store_key_value_store(self, data):
        take(directory)

        with open(f"{directory}/{key}", "w") as f:
            json.dump(data, f, indent=4)


if __name__ == '__main__':

    storage = KeyValueStoreClientImpl()

    storage.store_key_value_store({"data": "exists"})

    print(storage.get_key_value_store())
