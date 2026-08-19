class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=float('inf')
        ans=0
        for i in range(len(prices)):
            if prices[i]<min:
                min=prices[i]
            else:
                ans=max(ans, prices[i]-min)
        return ans
