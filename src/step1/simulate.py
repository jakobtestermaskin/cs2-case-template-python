from radio import handle


fake_data = [
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
    {
        "id": "3",
        "text": "But I've never felt this way for no one, oh",
        "type": "song",
        "song_name": "drivers license",
    },
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
    }
]


def simulate():
    handle(fake_data)


if __name__ == "__main__":
    simulate()
