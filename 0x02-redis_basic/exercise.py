#!/usr/bin/env python3
from uuid import uuid4
from typing import Union

import json
import redis

class Cache:
    """A simple Cache class that takes in a redis instance and flushes it"""
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()
        
    def store(self, data:Union[str,float,int,bytes])->str:
        """A method that takes in a data arguement, assigns a randomly generated key and returns that key"""
        key = str(uuid4())
        self._redis.set(key, json.dumps(data))
        return (key)

    def get(self, key, fn):
        self.fn = type(key)
        pass
