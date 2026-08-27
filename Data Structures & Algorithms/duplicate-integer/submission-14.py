class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     duplicate = set()
     for i in range (len(nums)):
            duplicate.add(nums[i])
     return len(nums) != len(duplicate)
    
