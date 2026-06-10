# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.m=-1
    def maxsum(self,root):
        r,l=0,0
        if root.left!=None:
            l=self.maxsum(root.left)
        if root.right!=None:
            r=self.maxsum(root.right)
        self.m=max(self.m,root.val,root.val+r+l,root.val+r,root.val+l)
        return max(root.val,root.val+r,root.val+l)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.m=root.val
        k=self.maxsum(root)
        return max(self.m,k)


        