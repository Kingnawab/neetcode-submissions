class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     duplicate = set(nums)
     return len(nums) != len(duplicate)
    
