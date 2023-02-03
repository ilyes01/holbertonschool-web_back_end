#!/usr/bin/env python3
import uuid
import redis
from typing import Optional, Callable, Union

class Cache:

    def __init__(self);
    """
    Constructor for the Cache class.
    Initializes a Redis connection and flushes any existing data.
    """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
    """
    Store a value in Redis.
    :param data: The value to be stored, can be a string, bytes, int, or float.
    :return: A random key generated using uuid to be used to retrieve the data later.
    """
        random_id = str(uuid.uuid4())
        self._redis.set(random_id, data)
        return random_id

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
    """
    Get a value from Redis, with the ability to convert the value to the original data type if desired.
    :param key: The key used to retrieve the value from Redis.
    :param fn: Optional callable to be used to convert the data back to the original data type.
    :return: The original data type of the value retrieved from Redis.
    """
        if fn:
            try:
                return fn(self._redis.get(key)) if fn else self._redis.get(key)
            except ValueError:
                raise ValueError("Cannot convert {value} to desired type.")

    def get_str(self, value: bytes) -> str:
    """
    Converts a byte string to a utf-8 encoded string.
    :param value: The byte string to be converted.
    :return: The converted utf-8 encoded string.
    """
    return value.decode("utf-8")

    def get_int(self, value: bytes) -> str:
    """
    Converts a byte string to an integer.
    :param value: The byte string to be converted.
    :return: The converted integer.
    """
        return int.from_bytes(value, sys.byteorder)

