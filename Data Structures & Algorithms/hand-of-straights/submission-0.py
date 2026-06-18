class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        
        d={}
        l=sorted(list(set(hand)))
        for j in range(n):
            if hand[j] in d:
                d[hand[j]]+=1
            else:
                d[hand[j]]=1
        
        k=0
        res=True
        m=0
        i=0
        for j in range(n):
            if (i==len(l)) or (l[i]+k not in d) or (d[l[i]+k]==0):
                res=False
                break
            else:
                d[l[i]+k]-=1
                if d[l[i]+k]==0:
                    m+=1
            k+=1
            if (j+1)%groupSize==0:
                k=0
                i=m
        return res
    



        
        

        
        