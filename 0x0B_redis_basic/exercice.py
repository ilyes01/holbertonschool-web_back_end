#!/usr/bin/env python3
import functools

class Cache:
    def store(self, value):
        key = str(hash(value))
        self._data[key] = value
        return key

    def get(self, key, fn=None):
        if key not in self._data:
            return None
        data = self._data[key]
        if fn:
            return fn(data)
        return data

    def get_str(self, key):
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key):
        return self.get(key, fn=int)

    _data = {}
import functools

class Cache:
    def store(self, value):
        key = str(hash(value))
        self._data[key] = value
        return key

    def get(self, key, fn=None):
        if key not in self._data:
            return None
        data = self._data[key]
        if fn:
            return fn(data)
        return data

    def get_str(self, key):
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key):
        return self.get(key, fn=int)

    _data = {}

