class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)): 
            product = 1  # start at  1
            for j in range(len(nums)):  # loop again to multiply all but nums[i]
                if i != j:  # skip itself
                    product *= nums[j]
            output.append(product)  # add the product to output list
        return output

        