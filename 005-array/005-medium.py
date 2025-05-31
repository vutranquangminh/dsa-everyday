class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        arr = []   
        for key,value in count.items():
            arr.append([key,value])

        def get_value(arr):
            return arr[1]
        
        arr.sort(key=get_value, reverse=True)

        anwser = []
        for i in range(k):
            anwser.append(arr[i][0])
            
        return anwser
