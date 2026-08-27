class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_count = {0:1}
        acc = 0
        for num in nums:
            acc += num
            target = acc - k
            result += prefix_count.get(target,0)
            prefix_count[acc] = 1 + prefix_count.get(acc,0)  
        return result




        