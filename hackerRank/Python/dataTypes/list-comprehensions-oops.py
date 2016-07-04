class base(object):
	def __init__(self):
		pass
	def coordinates(self,x,y,z,n):
		m=[]
		for i in range(x+1):
			for j in range(y+1):
				for k in range(z+1):
					if (i+j+k)!=n:
						m.append([i,j,k])
		print m

obj=base()

obj.coordinates(int(raw_input()),int(raw_input()),int(raw_input()),int(raw_input()))
