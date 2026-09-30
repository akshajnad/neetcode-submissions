class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            count = freq[num]
        
        arr = sorted(freq.values(), reverse=True)[0:k]
        result = []
        
        for key in freq:
            index = 0
            found = False
            while freq[key] in arr and index < len(arr):
                if arr[index] != freq[key]:
                    index += 1
                else:
                    found = True
                    break
            if found:
                arr.pop(index)
                result.append(key)
        return result