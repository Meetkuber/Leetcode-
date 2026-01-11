class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        m=1
        c=1
        if(len(nums)==0):
            return 0
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]):
                continue
            elif(nums[i-1]+1==nums[i]):
                c+=1
                if(m<c):
                    m=c
            else:
                c=1
        return m
        