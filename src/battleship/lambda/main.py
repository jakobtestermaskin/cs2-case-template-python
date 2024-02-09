import sys
import urllib.parse
import json

sys.path.append("./..")

# from move import move
# from arrange import arrange_boats

from move import shoot_coordinate
from arrange import arrange_boats
from groupdisplayconfig import get_group_display_config
from cell import CellState
from grid import initial_grid


def handler(event, context):
    http = event["requestContext"]["http"]
    method = http["method"]

    parsed_path = urllib.parse.urlparse(http["path"])

    path = parsed_path.path
    splitted_path = path.split("/")

    print(path)

    print(splitted_path)

    print("Received event on path %s with method: %s" % (path, method))

    def ok(body: dict):
        return {
            "statusCode": 200,
            "body": json.dumps(body),
            "headers": {
                "Content-Type": "application/json",
            },
        }

    def not_found():
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Not Found"}),
            "headers": {
                "Content-Type": "application/json",
            },
        }

    if method == "POST":  # then we want to find out what is next move
        body = json.loads(event["body"])
        print(body)

        if splitted_path[1] == "move":
            board = body["board"]
            life = body["life"]

            for row in range(len(board)):
                for column in range(len(board[row])):
                    board[row][column] = CellState(board[row][column])

            return ok(shoot_coordinate(grid=board))

        elif splitted_path[1] == "arrange":
            grid_size = body["gridSize"]

            boat_sizes = body["boatSizes"]

            grid = initial_grid(grid_size)

            return ok({"boats": arrange_boats(grid=grid, boat_sizes=boat_sizes)})

    elif method == "GET":
        if splitted_path[1] == "name":
            return ok(get_group_display_config())

    return not_found()


# @api.route("/move", methods=["POST"])
# def handle_next_move():
#     print("Handle next move")

#     board = request.json["board"]
#     life = request.json["life"]

#     for row in range(len(board)):
#         for column in range(len(board[row])):
#             board[row][column] = CellState(board[row][column])

#     shoot = shoot_coordinate(grid=board)

#     print("shoot", shoot)

#     return shoot


# @api.route("/arrange", methods=["POST"])
# def arrange_boats():

#     grid_size = request.json["gridSize"]

#     boat_sizes = request.json["boatSizes"]

#     gird = initial_grid(grid_size)

#     print(boat_sizes)

#     result = ab(grid=gird, boat_sizes=boat_sizes)
#     return {"boats": result}


# @api.route("/name", methods=["GET"])
# def group_name():
#     return get_group_display_config()
