class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sett=set(nums)
        return len(sett)!=len(nums)

