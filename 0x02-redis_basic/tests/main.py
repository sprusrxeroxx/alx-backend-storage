#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('0x02-redis_basic.exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
