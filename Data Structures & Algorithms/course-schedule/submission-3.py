class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=len(prerequisites)
        child=[[] for _ in range(numCourses)]
        for j in range(n):
            child[prerequisites[j][0]].append(prerequisites[j][1])
        
        def dfs(j):
            q=[j]
            visited=set()
            while(q):
                curr=q.pop()
                visited.add(curr)
                if len(child[curr])==0:
                    visited=set()
                    continue
                for x in child[curr]:
                    if x in visited:
                        return False
                    q.append(x)
            return True

        #print(child)
        for j in range(numCourses):
            if len(child[j]) and (not dfs(j)):
                #print(j)
                return False
        
        return True
