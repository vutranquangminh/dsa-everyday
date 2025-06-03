class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        noise = {}
        for n in nums:
            if n in noise:
                noise[n] += 1
            else:
                noise[n] = 1
        
        arr = []
        for key in noise:
            arr.append(int(key))

        arr = sorted(arr)
        total = 1
        compair = 1
        size = len(arr) - 1

        if len(arr) == 0:
            return 0

        for i in range(size):
            if arr[i] + 1 == arr[i+1]:
                compair += 1
                if compair > total:
                    total = compair
            else:
                compair = 1

        return total