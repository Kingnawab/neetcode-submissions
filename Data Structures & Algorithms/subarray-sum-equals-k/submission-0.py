class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = {0:1}
        current_sum = 0
        for i in nums:
            current_sum += i
            target = current_sum - k
            result += prefix_sum.get(target,0)
            prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum,0)
        return result
        