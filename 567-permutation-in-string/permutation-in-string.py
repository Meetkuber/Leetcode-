from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
            
        s1_count = Counter(s1)
        window_count = Counter(s2[:n1])

        if s1_count == window_count:
            return True

        for i in range(n1, n2):
            window_count[s2[i]] += 1

            leftchar = s2[i - n1]
            window_count[leftchar] -= 1
            if window_count[leftchar] == 0:
                del window_count[leftchar]

            if s1_count == window_count:
                return True

        return False