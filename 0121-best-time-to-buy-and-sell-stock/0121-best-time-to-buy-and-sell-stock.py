class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        ans=0
        for i in prices:
            if i<min:
                min=i
            profit=i-min
            if ans<profit:
                ans=profit
        return ans
