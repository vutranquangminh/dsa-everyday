class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        for i in range(len(nums)):
            numbers = nums[:]
            numbers.pop(i)
            target = -int(nums[i])
            left = 0
            right = len(numbers) - 1
            while left < right:
                total = numbers[left] + numbers[right]
                if total == target:
                    sub = []
                    sub.append(numbers[left])
                    sub.append(numbers[right])
                    sub.append(nums[i])
                    sub.sort()
                    if sub not in arr:
                        arr.append(sub)
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:    
                    right -= 1

        return arr