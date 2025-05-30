class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        compare_arr = []
        anwser_arr = []
        for i in range(len(strs)):
            check_arr = sorted(strs[i])
            if check_arr not in compare_arr:
                compare_arr.append(check_arr)
                ana_arr = []
                ana_arr.append(strs[i])
                for j in range(i+1,len(strs)):
                    sort_arr = sorted(strs[j])
                    if check_arr == sort_arr:
                        ana_arr.append(strs[j])
                anwser_arr.append(ana_arr)

        return anwser_arr