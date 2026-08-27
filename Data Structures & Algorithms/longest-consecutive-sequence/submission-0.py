class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        max_length = 0
        for i in set_num:
            if (i - 1) not in set_num:
                length = 1
                while (i + length) in set_num:
                    length +=1
                max_length = max(max_length,length)
        return max_length
        