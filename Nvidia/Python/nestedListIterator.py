# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = nestedList
        self.val_list = []
        
        while self.list:
            
            nl = self.list.pop(0)
            if(nl.isInteger()):
                self.val_list.append(nl.getInteger())
            else:
                new_list = nl.getList()
                new_list = new_list[::-1]
                for i in new_list:
                    self.list.insert(0,i)
        
    
        
    
    def next(self) -> int:
        return self.val_list.pop(0)
        
        
        
    
    def hasNext(self) -> bool:
        if(self.val_list):
            return True
        else:
            return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())