class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        
        child=[[] for _ in range(n)]
        for j in range(n-1):
            child[edges[j][0]].append(edges[j][1])
            child[edges[j][1]].append(edges[j][0])
        
        q=[0]
        visited=set()
        while(q):
            curr=q.pop()
            visited.add(curr)
            for x in child[curr]:
                if x not in visited:
                    q.append(x)
        if len(visited)==n:
            return True
        else:
            return False


        
        