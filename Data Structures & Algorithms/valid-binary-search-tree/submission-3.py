# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev=-float('inf')
        self.res=True
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            if self.prev>=node.val:
                self.res=False
                return
            self.prev=node.val
            #self.res=self.res and (not(len(l)>1 and l[-1]<=l[-2]))
            inorder(node.right)
        
        inorder(root)
        return self.res







