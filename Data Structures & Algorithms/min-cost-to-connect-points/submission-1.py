class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        n=len(points)
        q=[]
        parent={}
        for i in range(n):
            parent[i]=i
            for j in range(i+1,n):
                heapq.heappush(q,(abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i,j))

        def findparent(v):
            if parent[v]==v:
                return v
            parent[v]=findparent(parent[v])
            return parent[v]
        def union(x,y):
            rootx=findparent(x)
            rooty=findparent(y)
            if rootx!=rooty:
                parent[rooty]=rootx
                return True
            return False

        #visited=set()
        count=0
        cost=0
        while(count!=n-1):
            dist,x,y=heapq.heappop(q)
            if union(x,y):
                count+=1
                cost+=dist
        return cost


