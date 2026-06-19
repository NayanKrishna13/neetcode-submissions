class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        n=len(s)
        for j in range(n):
            d[s[j]]=j
        
        m=0
        i=-1
        l=[]
        for j in range(n):
            m=max(m,d[s[j]])
            if m==j:
                l.append(m-i)
                i=j
                m=0
        return l



                    