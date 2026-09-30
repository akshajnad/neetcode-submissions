class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsSort = []
        for i in range(len(strs)):
            strsSort.append("".join(sorted(strs[i])))
        result = [[]]
        ans = [[]]
        for i in range(len(strsSort)):
            word = strsSort[i]
            real = strs[i]
            index = 0
            found = True
            while word not in result[index]:
                if index == len(result) - 1:
                    found = False
                    break
                index += 1
            if found:
                result[index].append(word)
                ans[index].append(real)
            else:
                result.append([word])
                ans.append([real])
        ans.pop(0)
        return ans
        