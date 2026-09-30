class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(i, path, curr):
            if curr == 0:
                result.append(path.copy())
                return
            if curr < 0:
                return
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j, path, curr-nums[j])
                path.pop()

        result = []
        backtrack(0, [], target)
        return result
                