class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax=currmin=ans=nums[0]

        for i in range(1,len(nums)):
            curr=nums[i]
            if curr<0:
                currmax,currmin=currmin,currmax
            currmax= max(curr, curr*currmax)
            currmin= min(curr, curr*currmin)

            ans=max(ans,currmax)

        return ans