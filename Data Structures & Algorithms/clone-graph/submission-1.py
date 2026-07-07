
class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None
        old_to_new = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr=queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new[curr].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]


        
        