import random 
"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

"""

class RandomizedSet:

    def __init__(self):
        self.values = {}
        

    def insert(self, val: int) -> bool:
        if(self.values.get(val,0)):
            return False
        else:
            self.values[val]=1
            return True

    def remove(self, val: int) -> bool:
        if(self.values.get(val,0)):
            del self.values[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        num_indexes = len(self.values.values())
        rand = random.randint(0,num_indexes-1)
        return list(self.values.keys())[rand]