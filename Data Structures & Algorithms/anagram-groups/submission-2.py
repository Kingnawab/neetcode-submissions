class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # this is because we dont have the key as we are traversing so we should add it
        for string in strs:
            count = [0] * 26 # for each alphabet
            for character in string: #traverse each word
                count[ord(character) - ord("a")] +=1 # we need to know where in the array to put it
            result[tuple(count)].append(string)
        return  list(result.values())