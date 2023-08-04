from collections import deque

# we use queues for bfs because we need the FIFO functionality.
# The FIFO concept that underlies a Queue will ensure that those things
# that were discovered first will be explored first.


def bfs(root):
    queue = deque()

    if root:
        queue.append(root)  # first in

    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()  # first out
            print(curr.val)
            if curr.left:
                queue. append(curr.left)
            if curr.right:
                queue.append(curr.right)
    level += 1
