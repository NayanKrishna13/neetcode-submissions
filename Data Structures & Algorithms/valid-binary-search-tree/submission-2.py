# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l=[]
        self.res=True
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            l.append(node.val)
            self.res=self.res and (not(len(l)>1 and l[-1]<=l[-2]))
            inorder(node.right)
        
        inorder(root)
        return self.res







