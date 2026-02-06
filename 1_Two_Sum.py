class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []

# using hash maps {}

class Solution(object):
    def twoSum(self, nums, target):

        d = {}

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in d:
                return [d[diff], i]
            else:
                d[n] = i


        
        
