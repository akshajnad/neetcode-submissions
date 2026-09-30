class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        curr = 0
        best = 0
        freq = {}
        for r in range(len(s)):
            char = s[r]
            curr += 1
            freq[char] = freq.get(char, 0) + 1
            while curr - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
                curr -= 1
                    
            best = max(curr, best)
        return best