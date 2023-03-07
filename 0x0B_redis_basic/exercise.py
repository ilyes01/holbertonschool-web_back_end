#!/usr/bin/env python3
import redis
import functools
from typing import Callable

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            key = func.__qualname__
            self._redis.incr(key)
            return func(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data):
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=lambda x: int(x))
