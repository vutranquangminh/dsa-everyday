class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for m in s:
            if m.isalpha():
                arr.append(m.lower())
            elif m.isdigit():
                arr.append(m)

        size = int(round(len(arr)/2))
        left = []
        right = []
        for i in range(size):
            left.append(arr[i])
            reverse = -i-1
            right.append(arr[reverse])

        for j in range(size):
            if left[j] != right[j]:
                return False

        return True