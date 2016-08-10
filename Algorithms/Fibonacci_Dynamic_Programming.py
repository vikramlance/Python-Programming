'''

The Fibonacci numbers are the sequence of numbers defined by the linear recurrence equation

 F_n=F_(n-1)+F_(n-2) 	

with F_1=F_2=1

The Fibonacci numbers for n=1, 2, 3 , 4 ... are 1, 1, 2, 3, 5, 8, 13, 21, ..

This below program calculats N th Fibonacci number where N is provided as an input using dynamic programming.

'''
a=int(raw_input())

#Creat a dictionary to store the values of calculated Fibonacci numbers so that they can be used recursively
b={}

#function to calculate k th Fibonacci number
def f(k):
	if (k ==1) or (k==2):
		b[k]=1
	else:
		if k not in b.keys():
			for i in range(3,k+1):
				b[i] = f(i-1) + f(i-2)
		else:
			return b[k]
	return b[k]


print f(a)
