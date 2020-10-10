"""

"""

[ 00 01 02 03
  10 11 12 13
  20 21 22 23
  30 31 32 33]

  00 11 22 33 

  10 01 12 23

  20 11 02 13

  30 21 12 03


  0 0 1 2 3

matrix = [[1, 3, 2, 5],
          [3, 2, 5, 0],
          [9, 0, 1, 3],
          [6, 1, 0, 8]]


def bouncingDiagonals(matrix):

    n = len(matrix)
    # rows = len(matrix[0])
    for i in range(n):
        for j in range(n):

