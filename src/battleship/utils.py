import os
import builtins


def is_docker():
    """Check if the code is running inside a docker container.

    Returns:
        bool: True if the code is running inside a docker container.
    """
    return os.path.isfile("/.dockerenv")


def print(*args, **kwargs):
    if is_docker():
        return builtins.print(*args, **kwargs, flush=True)
    else:
        return builtins.print(*args, **kwargs)
