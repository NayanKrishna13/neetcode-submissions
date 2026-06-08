class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import deque
        dt,ds={},{}
        def checkequ():
            for j in dt.keys():
                if (j not in ds) or (dt[j]>ds[j]):
                    return False
            return True
            
        n1,n2=len(s),len(t)
        if n1<n2:
            return ""
        for j in range(n2):
            if t[j] in dt:
                dt[t[j]]+=1
            else:
                dt[t[j]]=1

        q=deque()
        i,j=0,0
        c=-1
        i1=0
        length=float('inf')
        while(j<n1):
            if s[j] in ds:
                ds[s[j]]+=1
            else:
                ds[s[j]]=1

            if s[j] in dt:
                q.append(j)
                if ds[s[j]]>dt[s[j]]:
                    if s[j]==s[q[0]]:
                        while(ds[s[q[0]]]>dt[s[q[0]]]):
                            ds[s[q[0]]]-=1
                            q.popleft()
                            i=q[0]
                if checkequ():
                    c=1
                    if length>j-i+1:
                        length=j-i+1
                        i1=i
            else:
                if not q:
                    i+=1
            j+=1
            #print("i,j,c:",i,j,c)
        if c==1:
            return s[i1:i1+length]
        else:
            return ""

            

        


        