from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(n) for n in nums]

        def compare(n1,n2):
            if n1 + n2 > n2+n1:
                return -1
            elif n2+n1 > n1+n2:
                return 1
            else :
                return 0

        nums_str.sort(key=cmp_to_key(compare))
        result = "".join(nums_str)

        if  result[0] == "0":
            return "0"
        return result
            