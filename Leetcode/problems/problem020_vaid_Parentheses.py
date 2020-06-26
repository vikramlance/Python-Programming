
from collections import deque

class solution:

    def is_valid(self, input_str):
        stack = [] # Can use stack = deque()
        paran_dict = {')': '(', '}': '{', ']': '['}

        for i in input_str:
            if i in paran_dict:
                if not stack or stack.pop() != paran_dict[i]:
                    return False
            else:
                stack.append(i)

        if stack:
            return False
        else:
            return True


input_str = "[{{}}])"

test = solution()

print(test.is_valid(input_str))
