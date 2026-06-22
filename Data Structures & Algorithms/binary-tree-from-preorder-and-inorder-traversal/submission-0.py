# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(inorder)
        root=TreeNode(preorder[0])
        q=[root]
        ind=0
        for j in range(1,n):
            node=TreeNode(preorder[j])
            if q[-1].val==inorder[ind]:
                while(q and q[-1].val==inorder[ind]):
                    p=q.pop()
                    ind+=1
                p.right=node
            else:
                q[-1].left=node
            q.append(node)
        return root
            