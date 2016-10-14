'''
1. in an array of consecutive integers (array is not sorted), there is one integer that is repeated. Find which one it is. 
(Try not to use if-else, and no new temp array)
	Input: 9,1,5,3,7,9,2,10,4,8,6
	output: 9
'''

class duplicateNumeber:
	def __init__(self,input):
		self.input = input
		
	
	def duplicateNum(self ):
		dupNum=sum(self.input) - sum(set(self.input))
		return dupNum
		
		
input= [9,1,5,3,7,9,2,10,4,8,6]
#output 9

findDup= duplicateNumeber(input)

print findDup.duplicateNum()
