from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 1. Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v, price in flights:
            adj[u].append((v, price))
            
        # 2. Distance array to track min cost to each city
        distance = [float('inf')] * n
        distance[src] = 0
        
        # 3. Queue stores: (current_node, current_cost)
        q = deque([(src, 0)])
        stops = 0
        
        # Loop until we run out of nodes or exceed k stops
        while q and stops <= k:
            size = len(q)
            # Create a snapshot/copy of distances for this level to avoid corruption
            next_distance = list(distance)
            
            for _ in range(size):
                curr_node, curr_cost = q.popleft()
                
                for neighbor, price in adj[curr_node]:
                    # If we found a cheaper way to get to the neighbor
                    if curr_cost + price < next_distance[neighbor]:
                        next_distance[neighbor] = curr_cost + price
                        q.append((neighbor, next_distance[neighbor]))
            
            # Update the main distance array after processing the entire level
            distance = next_distance
            stops += 1
            
        return distance[dst] if distance[dst] != float('inf') else -1