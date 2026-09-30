class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            result.append(n ** 2)
        return sorted(result)