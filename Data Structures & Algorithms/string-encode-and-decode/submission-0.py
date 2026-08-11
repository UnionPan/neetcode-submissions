class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)
            
        return "".join(encoded)
        

    def decode(self, s: str) -> List[str]:
        decoded = []
        length = 0
        i = 0
        while i < len(s):
            c = s[i]
            if (c >= '0' and c <= '9'):
                length = length * 10 + int(c)
                i += 1
                
            elif c == '#':
                decoded.append(s[i+1:i+1+length])
                i = i + length + 1
                length = 0

        return decoded