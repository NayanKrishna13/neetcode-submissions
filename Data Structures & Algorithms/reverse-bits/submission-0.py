class Solution:
    def reverseBits(self, n: int) -> int:
        s=bin(n)[2:]
        s="0"*(32-len(s))+s
        s=s[::-1]
        return int(s,2)
        