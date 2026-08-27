class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_elem = {} # mapping value : index
        for i, n in enumerate(nums): # enumerate gives you the index and the value
            diff = target - n
            if diff in previous_elem:
                return [previous_elem[diff], i]
            previous_elem[n] = i
        return
    

        