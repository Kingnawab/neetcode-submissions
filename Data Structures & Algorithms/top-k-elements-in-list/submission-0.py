class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[]for i in range (len(nums)+ 1)] # since we are 0 indexing
        count = {} # max heap
        for key in nums:
            count[key] = count.get(key,0) + 1 #give the default value as 0 and then plus one for the first occurence
        for key, value in count.items():
            frequency[value].append(key) # so this for example puts 4 occurences of 8 in index 4
        result = []
        for i in range (len(frequency) -1,0,-1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result
        