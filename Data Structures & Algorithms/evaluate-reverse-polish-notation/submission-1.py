class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q=[]
        s={"+","-","/","*"}
        m=0
        for j in range(len(tokens)):
            if j==0:
                q.append(int(tokens[j]))
            else:
                if tokens[j] not in s:
                    #print(tokens[j])
                    q.append(int(tokens[j]))
                else:
                    if tokens[j]=="+":
                        k=q.pop()
                        q[-1]+=k
                    elif tokens[j]=="-":
                        k=q.pop()
                        q[-1]=q[-1]-k
                    elif tokens[j]=="*":
                        k=q.pop()
                        q[-1]=q[-1]*k
                    else:
                        k=q.pop()
                        q[-1]=int(q[-1]/k)
            #print(q)
        return q[-1]
                        
                    