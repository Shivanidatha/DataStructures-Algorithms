class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i,n in enumerate(nums):
            if target-n not in hm:
                hm[n]=i
            else:
                return [i,hm[target-n]]