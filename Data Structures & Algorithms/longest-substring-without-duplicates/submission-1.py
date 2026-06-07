class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        elif n==1:
            return 1

        d={}
        i,j=0,0
        length=0
        while(j<n):
            #print("i,j:",i,j)
            if s[j] in d:
                if d[s[j]]>=i:
                    length=max(length,j-i)
                    i=d[s[j]]+1
            d[s[j]]=j
            j+=1
            length=max(length,j-i)
        return length




        