class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            frequency[i] = frequency.get(i,0) + 1
        print(frequency)
        frequency = sorted(frequency.items(),key = lambda x:x[1], reverse = True)[:k]
        print(frequency)
        new_list = []
        for i in frequency:
            new_list.append(i[0])
        return new_list
