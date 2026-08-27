class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, n in enumerate (nums):
            result = target - n
            if result in index:
                return [index[result],i]
            else:
                index[n] = i
        return False
        