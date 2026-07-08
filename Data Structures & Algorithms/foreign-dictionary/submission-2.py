class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        from collections import deque
        n=len(words)
        if n==1:
            return words[0]
        
        succ=defaultdict(list)
        indegree=defaultdict(int)
        k=0
        def wordcheck(a,b):
            la,lb=len(a),len(b)
            m,j=min(la,lb),0
            k=j
            while(j<la+lb-m):
                if j<m:
                    if a[j]!=b[j] and k!=-1:
                        succ[a[j]].append(b[j])
                        indegree[b[j]]+=1
                        if a[j] not in indegree:
                            indegree[a[j]]=0
                        k=-1
                    else:
                        if b[j] not in indegree:
                            indegree[b[j]]=0
                else:
                    if m==la and (b[j] not in indegree):
                        indegree[b[j]]=0
                    elif m==lb and (a[j] not in indegree):
                        indegree[a[j]]=0
                j+=1


            if k!=-1 and (la!=lb) and m==lb:
                return False                                                    
            return True

        for j in range(1,n):
            if not wordcheck(words[j-1],words[j]):
                return ""
        
        print(succ)
        print(indegree)
        q=deque()
        for x in indegree:
            if indegree[x]==0:
                q.append(x)
        
        if len(q)==0:
            return ""
        ans=[]
        while(q):
            curr=q.popleft()
            ans.append(curr)
            for child in succ[curr]:
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
            print(q)
        if len(ans)!=len(indegree):
            return ""
        return ''.join(ans)











            
        
        
        
