from flask import Flask, request
from flask_cors import CORS
import sys


sys.path.append("./..")

# from move import move
from arrange import arrange_boats as ab
from groupdisplayconfig import get_group_display_config
from grid import initial_grid
from move import shoot_coordinate

from cell import CellState

# Must be imported after module have been appended

api = Flask(__name__)
CORS(api)


@api.route("/move", methods=["POST"])
def handle_next_move():
    print("Handle next move")

    board = request.json["board"]
    life = request.json["life"]

    for row in range(len(board)):
        for column in range(len(board[row])):
            board[row][column] = CellState(board[row][column])

    shoot = shoot_coordinate(grid=board)

    print("shoot", shoot)

    return shoot


@api.route("/arrange", methods=["POST"])
def arrange_boats():

    grid_size = request.json["gridSize"]

    boat_sizes = request.json["boatSizes"]

    gird = initial_grid(grid_size)

    print(boat_sizes)

    result = ab(grid=gird, boat_sizes=boat_sizes)
    return {"boats": result}


@api.route("/name", methods=["GET"])
def group_name():
    return get_group_display_config()


if __name__ == "__main__":
    api.run(host="localhost", port=8000)
