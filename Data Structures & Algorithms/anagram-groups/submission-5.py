class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #if you encounter non existent key make a list
        for string in strs:
            count = [0] * 26 # this is because we want to look at the frequency
            for char in string:
                count[ord(char) - ord('a')] +=1
            result[(tuple(count))].append(string)
        return list(result.values())
        
        