import random

random_names = ["Thomastoget?", "Sunroad", "Ivar Aasen", "IA"]


def get_group_display_config():
    return {"name": random.choice(random_names)}
