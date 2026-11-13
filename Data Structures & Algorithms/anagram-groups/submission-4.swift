class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var anagrams: [String: [String]] = [:]
        for word in strs {
            let anagram = String(word.sorted())
            anagrams[anagram, default: []].append(word)
        }
        return Array(anagrams.values)
    }
}
