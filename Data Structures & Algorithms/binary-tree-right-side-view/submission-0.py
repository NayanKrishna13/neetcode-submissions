# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        if not root:
            return l
        from collections import deque
        q=deque()
        q.append((root,0))
        visited=set()
        while(q):
            curr,level=q.popleft()
            if level not in visited:
                l.append(curr.val)
                visited.add(level)
            if curr.right:
                q.append((curr.right,level+1))
            if curr.left:
                q.append((curr.left,level+1))
        return l

        