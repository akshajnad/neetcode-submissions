class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = [str(sorted(s)) for s in strs]
        result = {}
        for i in range(len(strs)):
            result[sortedStrs[i]] = result.get(sortedStrs[i], [])
            result[sortedStrs[i]].append(strs[i])
        return list(result.values())


