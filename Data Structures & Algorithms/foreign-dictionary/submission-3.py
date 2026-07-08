from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # Step 1: Initialize graph structures for EVERY unique character
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for w in words for c in w}
        
        # Step 2: Build relationships by comparing adjacent pairs
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            
            # Check for invalid prefix rule: e.g., ["ape", "ap"]
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            # Find the first mismatch
            for j in range(min_len):
                if w1[j] != w2[j]:
                    # Avoid duplicate edges to keep in-degree accurate
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break # Stop at the first mismatch!
        
        # Step 3: Kahn's Algorithm (Topological Sort)
        q = deque([c for c in indegree if indegree[c] == 0])
        ans = []
        
        while q:
            curr = q.popleft()
            ans.append(curr)
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        # If ans doesn't contain all unique characters, a cycle exists
        if len(ans) < len(indegree):
            return ""
            
        return "".join(ans)