#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Project_name :     git
    File Name    :     LRU_cache_collectionsDict
    Description  :
    Author       :     chenhong
    date         :     2018/10/16

-------------------------------------------------
"""
__author__ = ''
import collections

# ***************************
#
# collections.OrderedDic实现LRU。
# 1、没有解决并发时多线程读写
# 2、没有设置过期时间
#
# **************************
class LRUCache:
    """
    :param size:
    """

    def __init__(self, size=5):
        """
        :param size:
        """
        self.size = size
        self.cache = collections.OrderedDict()

    def get(self, key):
        """
        :param key:
        :return:
        """
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
        else:
            val = None

        return val

    def set(self, key, val):
        """
        :param key:
        :param val:
        :return:
        """
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.size:
            self.cache.popitem(last=False)
        print(val)
        self.cache[key] = val


if __name__ == '__main__':
    cache = LRUCache(6)

    for i in range(10):
        cache.set(i, i)
    print(cache.cache)

    cache.set(5, 6)
    print(cache.cache)
