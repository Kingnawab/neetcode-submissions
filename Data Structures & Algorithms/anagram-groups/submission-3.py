class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list) # because when searching for a key instead of crashing it wont
        for string in strs:
            count = [0] * 26 # we need an array of size 26 so we can count the occurences of the letters
            for char in string:
                count[ord(char) - ord('a')] +=1
            answer[tuple(count)].append(string)
        return list(answer.values())

        
        