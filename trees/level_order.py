# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # initialising queue

        queue = deque()
        res = []

        queue.append(root)

        # now we have to add root to the queue

        while queue:  # queue can't be null for this
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)

            if level:
                res.append(level)

        return res
