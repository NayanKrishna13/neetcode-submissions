# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root==None:
            return False
        q=[root]
        while(q):
            curr=q.pop()
            if (curr.left==None and curr.right==None):
                if curr.val==targetSum:
                    return True
            if curr.left!=None:
                curr.left.val+=curr.val
                q.append(curr.left)
            if curr.right!=None:
                curr.right.val+=curr.val
                q.append(curr.right)
        
        return False
            

        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        
