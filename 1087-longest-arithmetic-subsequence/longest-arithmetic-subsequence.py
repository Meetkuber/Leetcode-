from collections import Counter
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for _ in nums]
        ans = 2
## i stays still while j moves all the rest elements
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = dp[j].get(d, 1) + 1 ## main logic (dp[j].get(d,1) checks is athere any sequence if yes return it else return 1)
                ans = max(ans, dp[i][d])
        return ans