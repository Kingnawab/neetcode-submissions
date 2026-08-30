from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = defaultdict(int)
        for i in nums:
            majority[i]+=1
        return max(majority, key=majority.get)
        