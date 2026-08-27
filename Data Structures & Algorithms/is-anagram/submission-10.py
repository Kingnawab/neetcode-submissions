class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for i in s:
            counter[i] = counter.get(i,0) + 1
        for x in t:
            if x not in counter: # check for key
                return False
            counter[x] -= 1
            if counter[x] < 0:
                return False
        return True
        
        