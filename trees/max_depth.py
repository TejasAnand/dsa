class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        # recursive dfs

        if not root:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1
