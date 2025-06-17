from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k

# ✅ Dữ liệu để debug
nums = [0, 0, 1, 1, 1, 2, 2, 3, 4, 4]
sol = Solution()
k = sol.removeDuplicates(nums)

# 🖨️ In kết quả để kiểm tra
print("k =", k)
print("nums[:k] =", nums[:k])
