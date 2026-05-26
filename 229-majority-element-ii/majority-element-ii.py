from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if not nums:
            return []

        threshold = n//3
        count = Counter(nums)


        result =[]

        for num,freq  in count.items():
            if freq>threshold:
                result.append(num)
        return result