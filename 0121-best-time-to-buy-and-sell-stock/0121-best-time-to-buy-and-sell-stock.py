class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=r=0
        profit=0
        ans=float("-inf")
        while r<len(prices):
            profit=prices[r]-prices[l]
            ans=max(ans,profit)
            if profit<=0:
                l=r           
            r+=1
        return ans
