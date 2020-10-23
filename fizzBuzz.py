'''
Using the programming language of your choice:
	
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
'''

for row in range(1,101):
    if row%15==0:
        print "FizzBuzz"
    elif row%3==0:
        print "Fizz"
    elif row%5==0:
        print "Buzz"
    else:
        print row
