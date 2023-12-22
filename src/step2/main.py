import json
from step2_handler import handle


def handler(event, context):
    handle()


if __name__ == '__main__':
    handler({}, {})
