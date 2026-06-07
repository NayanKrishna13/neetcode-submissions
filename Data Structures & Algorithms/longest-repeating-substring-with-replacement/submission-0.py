class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        d={}
        length=1
        i,j=0,0
        maxfreq=0
        while(j<n):
            print("i,j:",i,j)
            if s[j] in d:
                d[s[j]]+=1
            else:
                d[s[j]]=1
            maxfreq=max(maxfreq,d[s[j]])
            if j-i+1-maxfreq>k:
                d[s[i]]-=1
                i+=1
            length=max(length,j-i+1)
            j+=1
        return length

        

        