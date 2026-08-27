class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for a,b in zip (nums, nums[1:]):
            if a == b:
                return True
        return False
         