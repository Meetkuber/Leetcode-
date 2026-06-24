class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #b[i] max profit until last buy
        #s[i] max profit until last sell
        #s2 cooldown
        b = -10 ** 9 
        s = 0
        s2 = 0
        for i in range(len(prices)):
            b = max(b,s2-prices[i])
            s2 = s
            s = max(s,b+prices[i])
        return s