"""



wrong answer 

class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        

        from collections import deque
        stack = deque()
        visited = set()
        result = 0
        for node in range(n):
            print('ddddddd node result', node, result)
            if informTime[node] == 0:
                parent = manager[node]
                print('eeeeeeee', parent)

                if parent not in visited:
                    stack.append(parent)

                print('aaaaaaa parent, visited, stack', parent, list(visited), stack)
                    
                while stack:
                    curr_node = stack.pop()

                    if curr_node not in visited:
                        print('bbb curr_node, visited, stack', curr_node, list(visited), stack)
                        print('cccc manager[curr_node]', manager[curr_node])

                        visited.add(curr_node)
                        result += informTime[curr_node]
                        if manager[curr_node] != -1:                            
                            stack.append(manager[curr_node])
                            print('fffffff', stack)
                            
        return result

"""


class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        

        from collections import deque
        stack = deque()
        visited = set()
        result = 0
        len_manager = len(manager)

        graph = [[]]*len_manager
        
        # make adjecency list of a graph

        print(graph)

        root = None

        for i in range(len_manager):
            print (i)
            if manager[i] == -1:
                root = i
            else:
                print(graph[manager[i]])
                graph[manager[i]].append(i)

        print(graph)




# n = 1
# headID = 0 
# manager = [-1] 
# informTime = [0]

test = Solution()
# print(test.numOfMinutes(n, headID, manager, informTime))

n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]


print(test.numOfMinutes(n, headID, manager, informTime))


# n = 7
# headID = 6
# manager = [1,2,3,4,5,6,-1]
# informTime = [0,6,5,4,3,2,1]


# print(test.numOfMinutes(n, headID, manager, informTime))


# n = 15
# headID = 0
# manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
# informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]

# print(test.numOfMinutes(n, headID, manager, informTime))
