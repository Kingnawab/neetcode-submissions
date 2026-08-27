class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, v in enumerate(nums):
            difference = target - v
            if difference in values:
                new_list = [values[difference],i]
                return new_list
            else:
                values[v] = i
        