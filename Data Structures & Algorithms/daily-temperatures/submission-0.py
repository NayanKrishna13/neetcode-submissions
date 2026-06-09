class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q=[]
        result=[0]*len(temperatures)
        for j in range(len(temperatures)):
            if j==0:
                q.append(j)
            else:
                while(q and temperatures[q[-1]]<temperatures[j]):
                    k=q.pop()
                    result[k]=j-k
                q.append(j)
            #print(q)
                
        return result


        