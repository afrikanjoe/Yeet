"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""


from collections import OrderedDict
class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = OrderedDict()
        
    def get(self, key):
        val = -1
        if key in self.hashmap:
            self.hashmap.move_to_end(key)
            val = self.hashmap[key]
        print("Get")
        print(self.hashmap)
        return val
    
    def put(self, key, value):
        if key in self.hashmap:
            self.hashmap.move_to_end(key)
        self.hashmap[key] = value
        if len(self.hashmap) > self.capacity:    
            self.hashmap.popitem(last=False)
        print("Put")
        print(self.hashmap)