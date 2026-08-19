class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        ans=float('-inf')
        for r in range(len(nums)):
            sum+=nums[r]
            ans=max(ans,sum)
            if sum<0:
                sum=0            
        return ans