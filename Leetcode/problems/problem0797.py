"""

"""

class Solution:
    def allPathsSourceTarget(self, graph): 
        result = []      
        path = [0]        
        destination = len(graph) -1 
            
        def recur(curr_node):
            # If current node is destination node then append path to result by copying path to new list
            if curr_node == destination:
                # Append new list to the result, if we append path to the result, result will pop elements from 
                # the path elements inside the result as soon as we pop element from path, as path is passed by reference
                result.append(list(path)) 
                        
            else:
                # iterate over each node (vertex) in the list of current nodes neighbours
                for v in graph[curr_node]:                    
                    path.append(v)
                    recur(v)
                    path.pop()

        recur(0)
        return result

test = Solution()
graph = [[1,2],[3],[3],[]]
print(test.allPathsSourceTarget(graph))    
