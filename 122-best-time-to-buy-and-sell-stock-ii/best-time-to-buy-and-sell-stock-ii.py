class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profprices = 0 
        curprices = prices[0]


        for i in range(0,len(prices)):
            if curprices < prices[i]:
                profprices += prices[i] - curprices
            curprices = prices[i]
        return profprices