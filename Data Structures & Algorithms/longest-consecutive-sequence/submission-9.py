class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_num = set(nums) #eliminate duplicates cause theyre not necessary
        length = 0
        for n in new_num:
            if(n - 1) not in new_num: #aka the smallest number possible
                result = 1
                acc = 0 # to find the next n + 1 number
                while(n + (acc + 1)) in new_num:
                    result +=1
                    acc +=1
                length = max(length,result)
        return length
        