# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q=[root]
        res=False
        def check(curr,subRoot):
            if (not curr) and (not subRoot):
                return True
            if ((not curr) and (subRoot)) or ((not subRoot) and (curr)):
                return False
            if curr.val!=subRoot.val:
                return False
            return check(curr.left,subRoot.left) and check(curr.right,subRoot.right)
                
        while (q):
            curr=q.pop()
            if (curr.val==subRoot.val) and check(curr,subRoot):
                res=True
                break
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return res

        


        