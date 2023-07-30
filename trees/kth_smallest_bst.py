# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.counter = 0
        self.kth_smallest = 0

        def inorder(root):
            if not root:
                return

            inorder(root.left)

            self.counter += 1

            if self.counter == k:
                self.kth_smallest = root.val

            inorder(root.right)

        inorder(root)

        return self.kth_smallest
