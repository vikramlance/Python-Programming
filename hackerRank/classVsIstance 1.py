class Person:
    a=0
    m =0
    def __init__(self,initialAge):
        if initialAge<0:
            print "Age is not valid, setting age to 0."
            self.initialAge=0
        else:
            age= initialAge
            
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if Person.m < 13:
            print Person.m
            print "You are young."
        elif 13<= Person.m <18:
            print "You are a teenager."
        else:
            print "You are old."
        # Do some computations in here and print out the correct statement to the console

    def yearPasses(self):
        # Increment the age of the person in here
        Person.a= Person.a + 1
        m= Person.a+ age
        print (m)
        m=self.m

        
    



T=int(raw_input())
for i in range(0,T):
    age=int(raw_input())         
    p=Person(age)  
    p.amIOld()
    for j in range(0,3):
        p.yearPasses();        
    p.amIOld();
    print ""
