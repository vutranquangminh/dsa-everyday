class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf')
        result = []

        for i in range(len(list1)):
            if list1[i] in list2:
                j = list2.index(list1[i])
                total = i + j
                if total < min_sum:
                    min_sum = total
                    result = [list1[i]]
                elif total == min_sum:
                    result.append(list1[i])

        return result