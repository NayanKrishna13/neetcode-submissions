# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxheight=0
        def heightfinder(node):
            if not node:
                return 0
            
            left=heightfinder(node.left)
            right=heightfinder(node.right)
            self.maxheight=max(left+right,self.maxheight)
            return 1+max(left,right)
        heightfinder(root)
        return self.maxheight
            


        