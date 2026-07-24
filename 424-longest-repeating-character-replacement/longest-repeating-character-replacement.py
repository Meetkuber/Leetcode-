class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        max_len = 0
        
        for right in range(len(s)):
            # 1. Update frequency map
            count[s[right]] = count.get(s[right], 0) + 1
            
            # 2. Track maximum frequency seen in the window
            max_freq = max(max_freq, count[s[right]])
            
            # 3. If replacements needed exceed k, shrink window from left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            # 4. Update the longest valid window length
            max_len = max(max_len, right - left + 1)
            
        return max_len