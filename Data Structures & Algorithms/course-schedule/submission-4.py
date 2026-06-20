class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        n=len(prerequisites)
        child=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for j in range(n):
            child[prerequisites[j][1]].append(prerequisites[j][0])
            indegree[prerequisites[j][0]]+=1

        q=deque()
        for j in range(numCourses):
            if indegree[j]==0:
                q.append(j)

        coursestaken=0
        while(q):
            curr=q.popleft()
            coursestaken+=1
            for x in child[curr]:
                indegree[x]-=1
                if indegree[x]==0:
                    q.append(x)
        return coursestaken==numCourses
        
