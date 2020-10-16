"""
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

 

Example 1:



Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.
Example 2:



Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.
Example 3:

Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
 

Constraints:

2 <= n <= 100
0 <= roads.length <= n * (n - 1) / 2
roads[i].length == 2
0 <= ai, bi <= n-1
ai != bi
Each pair of cities has at most one road connecting them.

4
[[0,1],[0,3],[1,2],[1,3]]

5
[[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
"""

class solution():
    def maximal_network_rank(n, roads):

        # store city as a key and list of connected cities as value
        number_of_connected_roads = {}

        for j in roads:

            if j[0] in number_of_connected_roads:
                number_of_connected_roads[j[0]].append(j[1])
            else:
                number_of_connected_roads[j[0]] = [j[1]]

            if j[1] in number_of_connected_roads:
                number_of_connected_roads[j[1]].append(j[0])
            else:
                number_of_connected_roads[j[1]] = [j[0]]

        # find top 2 road counts and return the sum of them, if city is counted twice then count -1
        # 0:1,3 , 1:0,2,3 , 2:1 , 3:1 
        top_count = 0
        top_city = -1
        second_top_count = 0
        second_top_city = -1
        #  edge case is not consider where 2 cities have same number of roads but if they dont have connection then take those 2 ciities
        for k in number_of_connected_roads:
            if len(number_of_connected_roads[k]) >= top_count:
                second_top_count = top_count 
                second_top_city = top_city
                top_count = len(number_of_connected_roads[k])
                top_city = k
        flag = 0
        if second_top_city != -1 and top_city != -1:
            if top_city in number_of_connected_roads[second_top_city]:
                flag = 1


        return top_count + second_top_count - flag








