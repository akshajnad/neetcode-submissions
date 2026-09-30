class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + ","
        string += "#"
        string += "".join(strs) 
        return string
        
        
    def decode(self, s: str) -> List[str]:
        if s[0] == "#":
            return []
        i_prev = 0
        i = s.index(",")
        j = s.index("#") + 1
        result = []
        while True:
            result.append(s[j:j+int(s[i_prev:i])])
            j += int(s[i_prev:i])
            if s[i+1] == "#":
                break
            i += 1
            i_prev = i
            while s[i] != ",":
                i += 1
        return result