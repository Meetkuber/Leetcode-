class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unmatched_id = 0

        for num in nums:
            unmatched_id ^= num 
        return unmatched_id