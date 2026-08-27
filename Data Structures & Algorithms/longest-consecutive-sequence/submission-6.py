class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newnum = set(nums)
        length = 0
        for i in newnum:
            if (i-1) not in newnum:
                lengt = 0
                while(i + lengt) in newnum:
                    lengt +=1
                length = max(lengt,length)
        return length

                
                
            
        