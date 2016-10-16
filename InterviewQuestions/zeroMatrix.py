'''
Given a boolean matrix, update it so that if any cell is true, all the cells in that row and column are true.

eg. 

[true,  false, false]      [true,  true,  true ]
[false, false, false]  ->  [true,  false, false]
[false, false, false]      [true,  false, false]

'''

# Assuming True=1, False=0
a=[[1,0,0],[0,0,0],[0,0,0]]

n= len(a)
#b= [i,j for i,j in a.index(1)]
#print b
for i in range(n):
	for j in range(n):
		if a[i][j]==1:
			for k in range(n):
				#print i,j,k
				if a[i][k]==0:
					a[i][k]=11
				if a[k][j]==0:
					a[k][j]=11
for i in range(n):
	for j in range(n):
		if a[i][j]==11:
			a[i][j]=1

print a
