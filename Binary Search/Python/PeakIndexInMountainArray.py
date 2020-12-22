class Solution:
    @staticmethod
    def peakIndexInMountainArray(arr):
        index = 0
        maxi = arr[0]
        for i in range(1,len(arr)):
            if(arr[i]>maxi):
                maxi = arr[i]
                index = i
        return index

    @staticmethod
    def peakIndexInMountainArrayBinary(arr):
        high = len(arr)-1
        low = 0
        while(low<high):
            mid = high + low >> 1
            if(arr[mid]<arr[mid+1]):
                low = mid +1
            else:
                high = mid
        return low


if __name__=="__main__":
    inp = [24,69,100,99,79,78,67,36,26,19]
    print(Solution.peakIndexInMountainArray(inp))
    print(Solution.peakIndexInMountainArrayBinary(inp))
