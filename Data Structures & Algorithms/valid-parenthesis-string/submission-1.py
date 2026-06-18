class Solution:
    def checkValidString(self, s: str) -> bool:
        d={"(":0,"*":0,")":0}
        d1={"(":0,"*":0,")":0}
        n=len(s)
        res=True
        for j in range(n):
            d[s[j]]+=1
            d1[s[n-j-1]]+=1
            if d[")"]>d["("]:
                if d["*"]>0:
                    d["("]+=1
                    d["*"]-=1
                else:
                    res=False
                    break
            if d1["("]>d1[")"]:
                if d1["*"]>0:
                    d1[")"]+=1
                    d1["*"]-=1
                else:
                    res=False
                    break
        return res
            

        