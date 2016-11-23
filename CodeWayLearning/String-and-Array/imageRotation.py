'''
rotate matrix by ninty degrees
'''

class ImageRotation:
    def __init__(self, inputMatirx):
        self.inputMatirx = inputMatirx
    def rotateMatirxByNintyDegrees(self):
        transposeMatrix=self.transposeMatrix()
        rotatedMatirx = self.reverseRowsOfMatirx(transposeMatrix)
        return rotatedMatirx
        
        
    def transposeMatrix(self):
        n= len(self.inputMatirx)
        a=self.inputMatirx
        b=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    b[i].append(a[i][j])
                else:
                    b[i].append(a[j][i])
        return b
    def reverseRowsOfMatirx(self, matrix):
        b=matrix
        outputMatrix=[]
        for k in  range (len(b)):
            outputMatrix.append(b[k][::-1])
        return outputMatrix
originalMatrix = [[1,2,3],[4,5,6],[7,8,9]]
newMatrix= ImageRotation(originalMatrix)
print newMatrix.rotateMatirxByNintyDegrees()
