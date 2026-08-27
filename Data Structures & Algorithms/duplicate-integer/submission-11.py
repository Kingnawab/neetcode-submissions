class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       isSeen = set()
       for i in nums:
        if (i in isSeen):
            return True
        isSeen.add(i)
       return False
     
        

        