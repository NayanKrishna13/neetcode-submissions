class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)
        for x,y in tickets:
            adj[x].append(y)

        for x in adj:
            adj[x].sort(reverse=True)

        stack=["JFK"]
        path=[]
        while stack:
            curr=stack[-1]
            if adj[curr]:
                stack.append(adj[curr].pop())
            else:
                path.append(stack.pop())
        
        return path[::-1]


