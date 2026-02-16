class Solution:
    def maxProduct(self, a: List[int]) -> int:
        c1,c2=-1,-1
        n=len(a)
        if n==1:
            return a[0]
        n+=1
        a.append(0)
        pro=[1]*n
        for j in range(n):
            pro[j]=(pro[j-1] if pro[j-1]!=0 else 1)*(a[j])
        p=-1
        #print(pro)
        for j in range(n):
            if a[j]!=0:
                if a[j]<0:
                    if c1==-1:
                        c1=j
                    c2=j
            else:
                if j==0:
                    continue
                if pro[j-1]>0:
                    p=max(p,pro[j-1])
                else:
                    if c1==-1:
                        p=max(p,pro[-1])
                    elif (j-1)!=c1:
                        p=max(p,max(pro[c2-1],pro[j-1]//pro[c1]))
                    else:
                        p=max(p,max(pro[c2-1],0))
                c1=-1
            #print(p)
        
        return p
    





        
