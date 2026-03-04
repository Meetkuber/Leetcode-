class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      currentMin = currentMax = 1
      maxProd = nums[0]
      for num in nums:
        values = [num, num * currentMax, num * currentMin]
        currentMax, currentMin = max(values), min(values)
        maxProd = max(maxProd, currentMax)
      return maxProd

