class Solution(object):
    def majorityElement(self, nums):
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1 
            else:
                counter[num] = 1 
        
        max_count = -1 
        ans = -1 

        for key,val in counter.items():
            if val > max_count:
                max_count = val
                ans = key
        
        return ans
        
