class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var freq: [Character: Int] = [:]
        var length = 0
        var l = 0
        var best = 0
        let chars = Array(s)
        for char in chars {
            freq[char, default: 0] += 1
            length += 1
            while freq[char, default: 0] > 1 {
                freq[chars[l], default: 0] -= 1
                l += 1
                length -= 1
            }
            best = max(length, best) 
        }
        return best
    }
}
