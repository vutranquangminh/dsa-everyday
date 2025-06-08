class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        arr = []
        for i in range(len(s)):
            try:
                if s[i] in ['{','[','(']:
                    arr.append(s[i])
                elif s[i] == '}' and arr[-1] == '{':
                    arr.pop(-1)
                elif s[i] == ']' and arr[-1] == '[':
                    arr.pop(-1)
                elif s[i] == ')' and arr[-1] == '(':
                    arr.pop(-1)
                else:
                    return False
            except:
                return False    
        if len(arr) != 0:
            return False
        return True