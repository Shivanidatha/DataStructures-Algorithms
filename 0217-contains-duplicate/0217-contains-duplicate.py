class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm=set(nums)
        return len(hm) != len(nums)