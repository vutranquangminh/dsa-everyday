Input: nums = [1, 2, 3, 3]

Output: true

Input: nums = [1, 2, 3, 4]

Output: false


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            check = nums.count(num)
            if check > 1:
                return True
        return False