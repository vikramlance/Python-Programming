class Solution:
    def mostVisited(self, n, rounds):
        
        """
        n sectors on circular track 
        rounds - list of marathons 
        
        iterate through rounds and map sector visits count and increase the count. 
find the top count.
        
        [1,3,1,2]
        1 to 3
        3 to 1
        1 to 2
        """
        
        sectors = []
            
        for i in range(n):
            sectors.append(i+1)
        sec_visited = {}
        for j in range(len(rounds) - 1):
            print("aaaa")
            print(j, rounds[j], rounds[j+1] )
            if rounds[j+1] < rounds[j]:
                for k in range(rounds[j]+1,n+1,1 ):
                    
                    if k in sec_visited:
                        sec_visited[k] += 1
                    else:
                        sec_visited[k] = 1
                for m in range(1, rounds[j+1] + 1,1 ):
                    if m in sec_visited:
                        sec_visited[m] += 1
                    else:
                        sec_visited[m] = 1
                
            else:                
                for k in range(rounds[j]+1,rounds[j+1] + 1,1 ):
                    
                    if k in sec_visited:
                        sec_visited[k] += 1
                    else:
                        sec_visited[k] = 1
                print("bbbb")
                print(sec_visited)

        print(sec_visited)
        sec_visited[rounds[0]] += 1 
        max_visited_count = 0
        for p in sec_visited:
            if sec_visited[p] > max_visited_count:
                max_visited_count = sec_visited[p]
        print(max_visited_count )
        max_visited_sectors = []
        
        for q in sec_visited:
            if sec_visited[q] == max_visited_count:
                max_visited_sectors.append(q)
        print(max_visited_sectors)
        return sorted(max_visited_sectors)
            
            
test = Solution()

n = 4
rounds = [1,3,1,2]        
print(test.mostVisited(n,rounds))
