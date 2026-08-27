class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            counter = [0] * 26
            for char in string:
                counter[ord(char) - ord('a')] +=1
            result[tuple(counter)].append(string)
            print(result)
        return list(result.values())


        