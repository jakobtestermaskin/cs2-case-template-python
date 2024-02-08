import json
import urllib3
import sys

from config import config


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def green(msg):
    return f"{bcolors.OKGREEN}{msg}{bcolors.ENDC}"


def yellow(msg):
    return f"{bcolors.WARNING}{msg}{bcolors.ENDC}"


def red(msg):
    return f"{bcolors.FAIL}{msg}{bcolors.ENDC}"


try:
    arg = sys.argv[1]
except:
    arg = None


def get_status(groupNumber, step):
    http = urllib3.PoolManager()
    url = f"{config.get('logsFunctionUrl')}/{groupNumber}/status/{step}"
    response = http.request(
        "GET", url, headers={"Authorization": f"Bearer {config.get('accessToken')}"}
    )
    status = response.data.decode("utf-8")

    return json.loads(status)["status"]


def get_status_emoji(bool):
    return "✅" if bool else "❌"


def output_status_step_1(status):
    print("----------------")
    color = green if status["step1"] else red
    print(f"{color('Step 1!')}", end="")
    if status["step1"]:
        print(f" {green('✅')}")
    elif not status["step1"]:
        print()
        print(
            f"Events are published: {get_status_emoji(status['events_are_published'])}"
        )
        if status["events_are_published"]:
            print(
                f"Last song events for last duration was reported sucessfully: {get_status_emoji(status['last_radio_cycle_was_correct_for_songs'])}"
            )
            print(
                f"No failed events for last 3 radio cycles: {get_status_emoji(status['no_failed_song_events_for_last_three_cycles'])}"
            )
            print(
                f"Last event was delivered at expected time: {get_status_emoji(status['last_event_was_delivered_at_expected_time'])}"
            )
            print(
                f"All hints are published: {get_status_emoji(status['all_hints_are_present'])}"
            )


def output_status_step_2(status):
    print("----------------")
    color = green if status["step2"] else red
    print(f"{color('Step 2!')}", end="")
    if status["step2"]:
        print(f" {green('✅')}")
    elif not status["step2"]:
        print()
        print(f"Events are published: {get_status_emoji(status['receivedEvents'])}")
        if status["receivedEvents"]:
            print(
                f"Payments were correct for last radio cycle: {get_status_emoji(status['paymentIsCorrectForExpectedSongsDuringRadioCycle'])}"
            )


def get_events(groupNumber):
    http = urllib3.PoolManager()
    url = f"{config.get('logsFunctionUrl')}/{groupNumber}/events"
    response = http.request(
        "GET", url, headers={"Authorization": f"Bearer {config.get('accessToken')}"}
    )
    events = response.data.decode("utf-8")

    return json.loads(events)


def pretty_print_events(events, type):
    for event in events["events"]:
        if event["type"] == "event" and event["event"] == type:
            try:
                del event["data"]["group_number"]
            except:
                pass
            print(event["data"], end="\n")


if __name__ == "__main__":

    def usage_info(subcommand=None):
        if subcommand == "events":
            print(
                "Usage: python3 get_events.py events [hint|song_ended|payment]\nEither get hint events (step 1), song ended events (step 1) or payment events (step 2)"
            )
        else:
            print(
                "Usage: python3 get_events.py [events|status (1/2)]\nEither get the current status for step 1/2 or get events for step 1 or 2\nFor status. The step number is optional. "
            )

    if len(sys.argv) < 2:
        usage_info()
    elif sys.argv[1] == "events":
        if len(sys.argv) < 3:
            usage_info("events")
        else:
            events = get_events(config["groupNumber"])
            pretty_print_events(events, sys.argv[2])

    elif sys.argv[1] == "status":
        steps = ["1", "2"]
        if len(sys.argv) >= 3:
            steps = [sys.argv[2]]

        if "1" in steps:
            status = get_status(config["groupNumber"], 1)
            output_status_step_1(status)

        if "2" in steps:
            status = get_status(config["groupNumber"], 2)
            output_status_step_2(status)

    else:
        usage_info()
