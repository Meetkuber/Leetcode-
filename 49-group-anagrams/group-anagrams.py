from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)- ord('a')] += 1
            key = tuple(count)
            anagram_dict[key].append(s)
        return anagram_dict.values()

        
        