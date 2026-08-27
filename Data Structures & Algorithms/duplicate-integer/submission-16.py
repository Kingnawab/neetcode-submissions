class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = set()
        for i in nums:
            if i in new_nums:
                return True
            new_nums.add(i)
        return False