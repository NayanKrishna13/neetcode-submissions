# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        levels=[[root.val]]
        q=deque()
        q.append((root,0))
        while(q):
            curr,height=q.popleft()
            if (len(levels)==height+1) and (curr.left or curr.right):
                levels.append([])
            if curr.left:
                levels[-1].append(curr.left.val)
                q.append((curr.left,height+1))
            if curr.right:
                levels[-1].append(curr.right.val)
                q.append((curr.right,height+1))
        return levels


        