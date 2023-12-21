from radio import handle
from db.client import KeyValueClientMock
from db.keyValueStore import KeyValueStore


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


fake_data = [[
    {
        "id": "1",
        "text": "Start",
        "type": "hint",
        "song_name": None,
    },
    {"text": "How you ran to her", "type": "song", "song_name": "traitor"},
    {
        "id": "2",
        "text": "Enda ett",
        "type": "hint",
        "song_name": None,
    },
],
    [
    {
        "id": "3",
        "text": "But I've never felt this way for no one, oh",
        "type": "song",
        "song_name": "drivers license",
    },
],
    [
    {
        "id": "5",
        "text": "I guess you didn't mean what you wrote in that song about me",
        "type": "song",
        "song_name": "drivers license"
    },
    {
        "id": "6",
        "text": "Enda ett",
        "type": "hint",
        "song_name": None,
    },
    {
        "id": "7",
        "text": "'Cause it's always one step forward and three steps back",
        "type": "song",
        "song_name": "1 step forward 3 steps back"},
    {
        "id": "8",
        "text": "It's always one step forward and three steps back",
        "type": "song",
        "song_name": "1 step forward 3 steps back"
    },
        {
        "id": "9",
        "text": "Enda ett siste",
        "type": "hint",
        "song_name": None,
    }
]]


def simulate():
    from time import sleep
    for data in fake_data:
        print(f"{bcolors.OKGREEN}Calling handle:{bcolors.ENDC}")
        handle(data, store=KeyValueStore(KeyValueClientMock()))

        print(
            f"\n{bcolors.OKCYAN}Sleeping for 1 second before calling with next data{bcolors.ENDC}\n")
        sleep(1)

    print("Finished simulating")


if __name__ == "__main__":
    simulate()
