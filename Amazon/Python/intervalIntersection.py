"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
"""




class Solution:
    def intervalIntersection(self, firstList, secondList):
        int1 = [0,2]
        int2 = [1,5]
        
        result = []
        for int1 in firstList:
            for int2 in secondList:
                int3 = self.merge_intervals(int1,int2)
                if(int3[0]<=int3[1]):
                    result.append(int3)
                    continue
        return result
    
    def merge_intervals(self,interval1,interval2):
        
        return [max(interval1[0],interval2[0]),min(interval1[1],interval2[1])]


if __name__ == "__main__":
    int_list1 = [[3,5],[9,20]]
    int_list2 =[[4,5],[7,10],[11,12],[14,15],[16,20]]
    print(Solution().intervalIntersection(int_list1,int_list2))