"""
he median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

"""



class MedianFinder:

    def __init__(self):
        
        self.list = []
        self.sorted = False
        
        

    def addNum(self, num):
        self.list.append(num)
        self.sorted=False
        

    def findMedian(self):
        if(not self.sorted):
            self.list = sorted(self.list)
            self.sorted = True
        
        mid = int((0 + len(self.list)-1)/2)
        if(len(self.list)%2==0):
            return (self.list[mid] + self.list[mid+1])/2
        else:
            return self.list[mid]