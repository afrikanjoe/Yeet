def findDisappearedNumbersBruteForce(nums):
        return_list = list(range(1,len(nums)+1))
        for i in set(nums):
            try:
                return_list.remove(i)
            except:
                continue
        return return_list

def findDisappearedNumbers(self,nums):
    return_list = []
    for i in range(len(nums)):
        index = abs(nums[i])-1
        if (nums[index] > 0):
            nums[index]*=-1
                
    for i in range(len(nums)):
        if(nums[i]>0):
            return_list.append(i+1)
    return return_list