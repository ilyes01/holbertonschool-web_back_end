#!/usr/bin/env python3
""" webpy"""
import requests
import redis
import time
from functools import wraps

# Redis cache instance
redis_cache = redis.Redis()


def cache(url, content):
    """ Caches the content of a URL  """
    redis_cache.setex(url, 10, content)


def track_count(url):
    """ Tracks the number of times a URL was accessed """
    redis_cache.incr(f"count:{url}")


def cached_page(fn):
    """ caching  """
    @wraps(fn)
    def wrapper(url):
        content = redis_cache.get(url)
        if content:
            return content.decode()
        else:
            content = fn(url)
            cache(url, content)
            return content
    return wrapper


def tracked_page(fn):
    """ Tracking  """
    @wraps(fn)
    def wrapper(url):
        track_count(url)
        return fn(url)
    return wrapper


@cached_page
@tracked_page
def get_page(url: str) -> str:
    """ Return content of the URL """
    response = requests.get(url)
    return response.content.decode()
