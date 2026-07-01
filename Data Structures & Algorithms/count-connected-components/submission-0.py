class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        child=[[] for _ in range(n)]
        for j in range(len(edges)):
            child[edges[j][0]].append(edges[j][1])
            child[edges[j][1]].append(edges[j][0])
        visited=set()
        def dfs(i):
            q=[i]
            visited.add(i)
            while(q):
                curr=q.pop()
                for x in child[curr]:
                    if x not in visited:
                        q.append(x)
                        visited.add(x)

        
        num=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                num+=1
        return num
