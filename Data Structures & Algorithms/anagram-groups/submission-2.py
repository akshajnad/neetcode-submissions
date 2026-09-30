class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsSort = []
        for i in range(len(strs)):
            strsSort.append("".join(sorted(strs[i])))
        
        result = []
        hashmap = {}
        for i, word in enumerate(strsSort):
            if word not in hashmap:
                result.append([strs[i]])
                hashmap[word] = len(result) - 1
            else:
                result[hashmap[word]].append(strs[i])
        return result