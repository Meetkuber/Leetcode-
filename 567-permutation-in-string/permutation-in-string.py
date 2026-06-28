from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: If s1 is longer than s2, s2 can't contain s1's permutation
        if len(s1) > len(s2):
            return False
            
        s1_count = Counter(s1)
        
        # Check every substring in s2 that is the exact same length as s1
        for i in range(len(s2) - len(s1) + 1):
            # Slice s2 to get the current window
            sub_string = s2[i : i + len(s1)]
            
            # If the counts match, we found a permutation!
            if s1_count == Counter(sub_string):
                return True
                
        return False