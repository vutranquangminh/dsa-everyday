class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for m in s:
            if m not in s_dict:
                s_dict[m] = 1
            else:
                s_dict[m] += 1
        
        for n in t:
            if n not in t_dict:
                t_dict[n] = 1
            else:
                t_dict[n] += 1

        try: 
            for i in s_dict:
                if s_dict[i] != t_dict[i]:
                    return False
        except:
            return False
        return True