import sys

sys.path.append("./..")

from move import move
from arrange import arrange_boats


def handler(event, context):
    http = event["requestContext"]["http"]
    method = http["method"]
    print("Received event with method: %s" % method)

    if method == "POST":  # then we want to find out what is next move
        move()

    elif method == "GET":
        arrange_boats()
