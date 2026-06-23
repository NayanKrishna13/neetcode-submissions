# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from collections import deque
        q=deque()
        count=1
        q.append(root)
        while(q):
            curr=q.popleft()
            if curr.left:
                if curr.left.val>=curr.val:
                    count+=1
                else:
                    curr.left.val=curr.val
                q.append(curr.left)
            
            if curr.right:
                if curr.right.val>=curr.val:
                    count+=1
                else:
                    curr.right.val=curr.val
                q.append(curr.right)
            print(count)
            #q.append(curr.left)
        return count

        