#!/usr/bin/env python3
import redis
import functools
import json
from typing import Callable, Union
from functools import wraps

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(method: Callable) -> Callable:
        key = method.__qualname__

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    def call_history(method: Callable) -> Callable:
        key = method.__qualname__

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            inputs_key = f"{key}:inputs"
            outputs_key = f"{key}:outputs"
            self._redis.rpush(inputs_key, json.dumps(args))
            output = method(self, *args, **kwargs)
            self._redis.rpush(outputs_key, json.dumps(output))
            return output
        return wrapper

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
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

    def replay(method: Callable):
    key = method.__qualname__
    input_key = f"{key}:inputs"
    output_key = f"{key}:outputs"

    input_history = cache._redis.lrange(input_key, 0, -1)
    output_history = cache._redis.lrange(output_key, 0, -1)

    print(f"{key} was called {len(input_history)} times:")
    for inputs, output in zip(input_history, output_history):
        inputs = eval(inputs.decode())
        output = output.decode()
        print(f"{key}{inputs} -> {output}")
