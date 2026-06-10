# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        from collections import deque
        if root==None:
            return ""
        q=deque()
        l=[]
        q.append(root)
        l.append(str(root.val))
        while(q):
            curr=q.popleft()
            if not curr:
                continue
            if curr.left:
                l.append(str(curr.left.val))
            else:
                l.append("*")
            if curr.right:
                l.append(str(curr.right.val))
            else:
                l.append("*")
            q.append(curr.left)
            q.append(curr.right)
        return ",".join(l)
        
        
        
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=="":
            return None
        from collections import deque
        q=deque()
        l=data.split(",")
        print(l)
        n=len(l)
        root=TreeNode(int(l[0]))
        q.append(root)
        i=1
        for j in range(n):
            k=q.popleft()
            if l[j]!="*":
                if not k:
                    continue
                if l[i]=="*":
                    k.left=None
                else:
                    k.left=TreeNode(int(l[i]))                
                if l[i+1]=="*":
                    k.right=None
                else:
                    k.right=TreeNode(int(l[i+1]))
                print("j,i:",j,i)
                i+=2
                q.append(k.left)
                q.append(k.right)
        return root

                

        

