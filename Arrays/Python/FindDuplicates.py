class Solution:
    @staticmethod
    def findDuplicates(nums):
        returnarr = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if(nums[index]<0):
                returnarr.append(abs(nums[index]))
            else:
                nums[index] = nums[index]*-1
        return returnarr


if __name__ == "__main__":
    inp = [4,3,2,7,8,2,3,1]
    print(Solution.findDuplicates(inp))
            