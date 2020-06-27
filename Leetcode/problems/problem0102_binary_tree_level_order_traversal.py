"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

from collections import deque


class solution:
    def bfs(self, arr):
        result = []

        temp_queue = deque()

        temp_queue.append(arr[0])

        i = 0

        while temp_queue:
            current_level_list = []
            curr_size_temp_queue = len(temp_queue)

            for j in range(curr_size_temp_queue):
                current_node = temp_queue.popleft()
                # add children of current node to queue
                current_level_list.append(current_node)

                if (2 * i + 1) < len(arr) and arr[2 * i + 1]:
                    temp_queue.append(arr[2 * i + 1])

                if (2 * i + 2) < len(arr) and arr[2 * i + 2]:
                    temp_queue.append(arr[2 * i + 2])

                i += 1

            result.append(current_level_list)

        return result


arr = [3, 9, 20, None, None, 15, 7]
test = solution()

print(test.bfs(arr))
