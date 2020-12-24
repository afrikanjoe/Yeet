class Solution:
    @staticmethod
    def majorityElement(nums):
        count_dict = {}
        thresh = len(nums)/2
        for i in nums:
            count_dict[i] = count_dict.get(i,0)+1
            if(count_dict[i]>thresh):
                return (i)


if __name__=="__main__":
    inp = [3,2,3]
    print(Solution.majorityElement(inp))