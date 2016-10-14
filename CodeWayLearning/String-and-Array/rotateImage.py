class rotateImage:
    'common base class for roating a matrix'
    def __init__(self, originalMatrix):
        self.originalMatrix=originalMatrix
    def rotateImageByNintyDegrees(self):
        rotateMatrix = zip(*self.originalMatrix[::-1])
        print  rotateMatrix

originalMatrix = [[1,2,3],[4,5,6],[7,8,9]]
newMatrix = rotateImage(originalMatrix)
print newMatrix.rotateImageByNintyDegrees()
