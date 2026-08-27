class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # mapping the count from a-z of each string 
        for string in strs:
            count = [0] * 26 # one for each character in lowercase a-z
            for c in string:
                count[ord(c) - ord("a")] += 1 # this will allow us to map our character into our array count so a = 0 etc...
            result[tuple(count)].append(string)
        return list(result.values())
  