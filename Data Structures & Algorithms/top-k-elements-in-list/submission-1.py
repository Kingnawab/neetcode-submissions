class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for i in nums:
            result[i] = result.get(i,0) + 1
        result = list(result.items())
        result = sorted(result,key = lambda x:x[1], reverse = True)[:k]
        number = []
        for key in result:
            number.append(key[0])
        return number

        

    