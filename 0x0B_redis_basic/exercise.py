#!/usr/bin/env python3
"""
Exercise file
"""
from typing import Callable, Optional, Union
import redis
import uuid
import sys
from functools import wraps


def replay(fn):
    store = redis.Redis()
    count_key = fn.__qualname__
    input_key = count_key + ":inputs"
    output_key = count_key + ":outputs"
    count = store.get(count_key).decode("utf-8")
    print("{} was called {} times:".format(count_key, count))
    inputs = store.lrange(input_key, 0, int(count)-1)
    outputs = store.lrange(output_key, 0, int(count)-1)
    for input, output in zip(inputs, outputs):
        input = input.decode("utf-8")
        output = output.decode("utf-8")
        print("{}(*{}) -> {}".format(count_key, input, output))



def count_calls(method: Callable) -> Callable:
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    key = method.__qualname__
    input_key = key + ":inputs"
    output_key = key + ":outputs"


    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(input_key, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(data))
        return data
    return wrapper

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_id = str(uuid.uuid4())
        self._redis.set(random_id, data)
        return random_id

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_str(self, value: bytes) -> str:
        return value.decode("utf-8")
    def get_int(self, value: bytes) -> int:
        return int.from_bytes(value, sys.byteorder)
