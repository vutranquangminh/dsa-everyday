class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            check = nums.count(num)
            if check > 1:
                return True
        return False