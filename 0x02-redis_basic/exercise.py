#!/usr/bin/env python3
from uuid import uuid4
import redis

class Cache:
    """A simple Cache class that takes in a redis instance and flushes it"""
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()
        
    def store(self, data):
        """A method that takes in a data arguement, assigns a randomly generated key and returns that key"""
        self.key = str(uuid4())
        self.set(key, data)

        return (key)

    def get(self, key, fn):
        self.fn = type(key)
        
        pass
