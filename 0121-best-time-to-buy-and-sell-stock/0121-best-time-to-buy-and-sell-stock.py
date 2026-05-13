class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=float('inf')
        ans=0

        for i in range(len(prices)):
            if prices[i]<low:
                low=prices[i]
            profit=prices[i]-low
            ans=max(ans,profit)
        return ans