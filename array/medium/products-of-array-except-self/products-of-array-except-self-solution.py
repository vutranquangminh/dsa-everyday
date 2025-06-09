class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        skip = 0
        arr = []
        while skip < len(nums):
            mul = 1
            for i in range(len(nums)):
                if i == skip:
                    mul *= 1
                else:
                    mul *= nums[i]
            
            skip += 1
            arr.append(mul)
            
        return arr