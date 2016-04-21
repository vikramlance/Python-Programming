for row in range (1,101):
    if row%15==0:
        print "FizzBizz"
    elif row%3==0:
        print "Fizz"
    elif row%5==0:
        print "Bizz"
    else:
        print row
