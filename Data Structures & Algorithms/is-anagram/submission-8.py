class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        