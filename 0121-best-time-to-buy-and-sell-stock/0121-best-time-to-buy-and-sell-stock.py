class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        ans=0
        for i in prices:
            if i<min:
                min=i
            if ans<i-min:
                ans=i-min
        return ans
