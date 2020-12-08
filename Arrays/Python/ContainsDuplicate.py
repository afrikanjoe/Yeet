def containsDuplicate(nums):
    res = set(nums)
    return not (len(res)== len(nums))