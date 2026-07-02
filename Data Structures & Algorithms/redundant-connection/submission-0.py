class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # Nodes are 1-indexed up to n (which equals len(edges))
        n = len(edges)
        parent = list(range(n + 1))
        
        def find(v):
            if parent[v] == v:
                return v
            # Path compression optimization
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_b] = root_a
                return True
            return False
            
        for u, v in edges:
            if not union(u, v):
                return [u, v]