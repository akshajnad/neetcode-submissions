class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        curr = 0
        best = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            curr += 1
            while sum(list(freq.values())) - max(list(freq.values())) > k:
                freq[s[l]] -= 1
                l += 1
                curr -= 1
            best = max(curr, best)
        return best