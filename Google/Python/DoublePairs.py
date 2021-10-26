"""
Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] 
for every 0 <= i < len(arr) / 2, or false otherwise.
"""

from collections import Counter

class Solution:
    def canReorderDoubledTwo(self, arr):
        count = 0 
        arr = sorted(arr)
        while arr:
            if(arr):
                item = arr[0]
                double_item=2*item
                if(double_item in arr):
                    try:
                        arr.remove(double_item)
                        arr.remove(item)
                    except:
                        return False
                elif(double_item not in arr and item%2==0):
                    double_item=item/2
                    if(double_item in arr):
                        try:
                            arr.remove(double_item)
                            arr.remove(item)
                        except:
                            return False
                    else:
                        return False
                else:
                    return False      
            else:
                return True
            count+=1
        return len(arr)==0

    def canReorderDoubled(self, arr):
        dic=Counter(arr)
        #just map arr[i] with 2*arr[i]
        # sort by the absolute value. This is brilliant
        for i in sorted(arr,key=abs):
            if dic[i]==0:continue
            if dic[2*i]==0: return False
            if i==0 and dic[i]<=1:return False
            dic[i]-=1
            dic[2*i]-=1
        return True

if __name__ == "__main__":
    arr = [3,1,3,6]
    print(Solution().canReorderDoubled(arr))
    arr = [2,1,2,6]
    print(Solution().canReorderDoubled(arr))
    arr = [4,-2,2,-4]
    print(Solution().canReorderDoubled(arr))
    arr = [1,2,4,16,8,4]
    print(Solution().canReorderDoubled(arr))