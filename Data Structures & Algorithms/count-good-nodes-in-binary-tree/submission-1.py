# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxval=-101
        count=0
        q=[(root,maxval)]
        while(q):
            node,maxval=q.pop()
            if node.val>=maxval:
                count+=1
            current_max=max(node.val,maxval)
            if node.right:
                q.append((node.right,current_max))
            if node.left:
                q.append((node.left,current_max))
        return count
