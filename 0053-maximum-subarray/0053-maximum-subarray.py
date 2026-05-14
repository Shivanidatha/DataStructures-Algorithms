class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        ans=float('-inf')
        for i in range(len(nums)):
            curr+=nums[i]
            ans=max(ans,curr)    
            if curr<0:
                curr=0       
            
        return ans
