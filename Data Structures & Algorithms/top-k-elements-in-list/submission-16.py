from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        freqrev = defaultdict(list)
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            freqrev[freq[num]].append(num)
            if freq[num] > 1:
                freqrev[freq[num]-1].remove(num)
        values = [freqrev[freq] for freq in sorted(freqrev, reverse=True)]
        result = []
        for l in values:
            for val in l:
                result.append(val)
                if len(result) == k:
                    break
            if len(result) == k:
                break
        return result
