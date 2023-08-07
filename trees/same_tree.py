# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_res=[]
        q_res=[]

        self.preorder(p,p_res)
        self.preorder(q,q_res)

        if p_res==q_res:
            return True
        
        else:
            return False

    def preorder(self, root, res):
        if root:
            res.append(root.val)
            self.preorder(root.left, res)
            self.preorder(root.right,res)
        else:
            res.append(None)

    



            