class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        res = 0 
        for i in range(len(points) - 1):
            
            px = abs(points[i][0] - points[i+1][0])
            py = abs(points[i][1] - points[i+1][1]) 
            res += max(px,py)  
        return res