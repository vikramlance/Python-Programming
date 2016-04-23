'''

A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:


Sample Input

Heraldo Memelli 8135627
2
100 80
Sample Output

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O

'''

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber
#global scores
#scores = map(int, scores)
#scores=[]
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
                self.scores = scores
                self.firstName = firstName
                self.lastName = lastName
                self.idNumber = idNumber
                 
            
    def calculate(self):
            b=0
            for row in scores:
                    
                    b=b+ int(row) 
            a= b/numScores
            #print a
            if 90<=a<=100:
                    return "O"
            elif 80<=a<90:
                    return "E"
            elif 70<=a<80:
                    return "A"
            elif 55<=a<70:
                    return "P"
            elif 40<=a<55:
                    return "D"
            elif 0<=a<40:
                    return "T"
            else:
                    return "wrong average"
                                  
                    
line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = raw_input().split()
print scores
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
