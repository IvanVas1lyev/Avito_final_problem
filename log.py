from typing import Callable
from random import randint


def log(text: str) -> Callable:
    """Decorates function"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            print(text.format(randint(2, 5)))

            return ret

        return wrapper

    return decorator
