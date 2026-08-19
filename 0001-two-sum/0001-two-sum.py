class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,n in enumerate(nums):    
            hm[n]=i
        for i in range(len(nums)):
            if target-nums[i] in hm and i!=hm[target-nums[i]]:
                return [hm[target-nums[i]],i]
        