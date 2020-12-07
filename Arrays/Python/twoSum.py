def twoSumBruteForce(nums, target):
    keys = [(i,j) for i in range(len(nums)) for j in range(len(nums)) if i!=j]
    answer = []
    for key in keys:
        tot= nums[key[0]]+nums[key[1]]
        if(tot==target):
            answer.append(key[0])
            answer.append(key[1])
            break
    return answer


def twoSum(self, nums, target):
    num_set = {}
    for num_index, num in enumerate(nums):
        if (target-num) in num_set:
            return [num_set[target-num], num_index]
        num_set[num] = num_index