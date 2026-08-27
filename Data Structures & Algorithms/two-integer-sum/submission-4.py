class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We want to find the index of the two pairs
        #hashmap where the key = element and the value is the key
        value = {}
        for i, n in enumerate(nums):
            answer = target - n
            if answer in value:
                list1 = [value[answer],i]
                return list1
            else:
                value[n] = i

        