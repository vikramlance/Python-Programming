'''
Sample Input

4
-1
10
16
18
Sample Output

Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
'''

class Person:
    #a=0
    
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        
        if initialAge < 0:
            self.initialAge = 0
            print "Age is not valid, setting age to 0."
        else:
            self.initialAge = initialAge
        

    def yearPasses(self):
        
        # Increment the age of the person in here
        #Person.a= Person.a + 1
        #m= Person.a+ self.initialAge
                
        self.initialAge= 1 + self.initialAge
        
        
        #print m
        return self.initialAge
    
    def amIOld(self):
        k=self.yearPasses()
        # Do some computations in here and print out the correct statement to the console
        if (k-1) < 13:
            #print k
            print "You are young."
        elif 13<= (k-1) <18:
            print "You are a teenager."
        else:
            print "You are old."
    



T=int(raw_input())
for i in range(0,T):
    age=int(raw_input())         
    p=Person(age)  
    p.amIOld()
    for j in range(0,3):
        p.yearPasses();        
    p.amIOld();
    print ""
