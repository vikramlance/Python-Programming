"""
733. Flood Fill

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].



        from collections import deque

        stack = deque()
        stack.append((sr,sc))

        old_color = image[sr][sc]

        # image[sr][sc] = newColor


        while stack:

            node = stack.pop()        

            x = node[0]
            y = node[1]
            image[x][y] = newColor

            # children = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
            
            children = []

            if x + 1 < len(image):
                children.append((x+1,y))

            if x - 1 >= 0:
                children.append((x-1,y))

            if y + 1 < len(image[0]):
                children.append((x+1,y))

            if y - 1 >= 0:
                children.append((x+1,y))

            for i in children:
                if image[i[0]][i[1]] == old_color:
                    
                    stack.append(i)

        return image    

"""


class Solution:
    def floodFill(self, image, sr, sc, newColor):


        from collections import deque

        stack = deque()
        stack.append((sr,sc))

        old_color = image[sr][sc]
        if old_color == newColor:
            return image

        while stack:

            node = stack.pop()        

            x = node[0]
            y = node[1]
            
            image[x][y] = newColor 


            if x + 1 < len(image) and image[x+1][y] == old_color:
                stack.append((x+1,y))                   

            if x - 1 >= 0 and image[x-1][y] == old_color:
                stack.append((x-1,y))    

            if y + 1 < len(image[0]) and image[x][y+1] == old_color:
                stack.append((x,y +1))    

            if y - 1 >= 0 and image[x][y -1] == old_color:
                stack.append((x,y-1))          

        return image      
