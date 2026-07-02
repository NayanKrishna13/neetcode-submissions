class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        n=len(points)
        q=[]
        parent={}
        for i in range(n):
            parent[(points[i][0],points[i][1])]=(points[i][0],points[i][1])
            for j in range(i+1,n):
                heapq.heappush(q,(abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),tuple(points[i]),tuple(points[j])))

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
        cost=0
        while(q):
            dist,x,y=heapq.heappop(q)
            if union(x,y):
                cost+=dist
        return cost


