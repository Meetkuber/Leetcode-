class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = float('-inf')
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            total = max(cur_sum,total)

            if cur_sum < 0:
                cur_sum = 0

        return total