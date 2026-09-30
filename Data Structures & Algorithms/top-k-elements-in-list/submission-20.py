from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num, count in counts.items():
            freq[count].append(num)
        result = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    break
            if len(result) == k:
                break
        return result
        """
        freq = {}
        freqrev = defaultdict(list)
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            freqrev[freq[num]].append(num)
            if freq[num] > 1:
                freqrev[freq[num]-1].remove(num)
        values = [freqrev[freq] for freq in sorted(freqrev, reverse=True)]
        result = []
        for freqlist in values:
            for val in freqlist:
                result.append(val)
                if len(result) == k:
                    break
            if len(result) == k:
                break
        return result
        """
