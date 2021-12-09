"""
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. 
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.


"""

class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        
        count = 0 
        units = 0
        boxTypes = sorted([[i[1],i[0]] for i in boxTypes])
        while truckSize>0 and len(boxTypes)>0:
            top_box = boxTypes[-1]
            for i in range(min(truckSize,top_box[1])):
                if(truckSize>0):
                    units+= top_box[0]
                    truckSize-=1
            boxTypes.pop()
                
                
        return units


if __name__ == "__main__":
    boxes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    print(Solution().maximumUnits(boxes,truckSize))