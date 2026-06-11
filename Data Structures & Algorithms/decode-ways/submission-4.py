class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        # prev2 represents dfs(j+2), prev1 represents dfs(j+1)
        prev2, prev1 = 1, 1
        
        for i in range(1, len(s)):
            current = 0
            # Single digit decoding (like your l > 0)
            if s[i] != "0":
                current += prev1
            
            # Two digit decoding (like your r <= 26)
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
                
            if current == 0:
                return 0
            
            prev2 = prev1
            prev1 = current
            
        return prev1