#!/usr/bin/env python3
from uuid import uuid4
from typing import Union, Callable

import redis

class Cache:
    """A simple Cache class that takes in a redis instance and flushes it"""
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()
        
    def store(self, data:Union[str, bytes, int, float])->str:
        """A method that takes in a data arguement, assigns a randomly generated key and returns that key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return (key)

    def get(self, key, fn:Callable==None)->Union[any, None]:
        try:
            data = self._redis.get(key)
            
            if data is None:
                return None

            if fn:
                return fn(data)
                
            else:
                return data

        except Exception as e:
            print("Error retrieving data : {e}")
            return None

    def get_str(self, key: str) -> str:
        """Retrieves data from Redis as a string."""
        value = self.get(key)
        if value is None:
            return ""  # Or handle missing value as needed
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """Retrieves data from Redis as an integer."""
        value = self.get(key)
        if value is None:
            return 0  # Or handle missing value as needed
        return int(value)