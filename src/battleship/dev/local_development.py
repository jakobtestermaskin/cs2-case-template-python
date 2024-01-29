from flask import Flask, request
from flask_cors import CORS
import sys


sys.path.append("./..")

from move import move
from arrange import arrange_boats as ab

# Must be imported after module have been appended

api = Flask(__name__)
CORS(api)


@api.route("/", methods=["POST"])
def handle_next_move():
    return move()


@api.route("/", methods=["GET"])
def arrange_boats():
    return ab()


if __name__ == "__main__":
    api.run(host="localhost", port=8000)
