print("hello")
a = 5
b = 6

print(a + b)

# name = input("What is your name? ")
# print('Hello ' + name)


if a == 5:
    print("wow")


city = ['Tokyo', 'New York', 'Toronto', 'Hong Kong']
print('Cities loop:')
for i in range(len(city)):
    print('City: ' + city[i])


def func_name(x, y):
    return x * y


print(func_name(3, 4))


words = {'a': 1, 't': [2, 3, 6]}
words["BMP"] = "Bitmap"
words["BTW"] = "By The Way"
words["BRB"] = "Be Right Back"

print(words)
print(words["BRB"])
print(words['t'])


filename = "file.txt"

with open(filename) as f:
    content = f.readlines()

print(content)


filename = "file.txt"

infile = open(filename, 'r')
data = infile.read()
infile.close()

print(data)


balance = 7


def addAmount(x):
    global balance
    balance = balance + x


addAmount(5)
print(balance)


import time

timenow = time.localtime(time.time())
year, month, day, hour, minute = timenow[0:5]

print(str(day) + "/" + str(month) + "/" + str(year))
print(str(hour) + ":" + str(minute))

print("Hello")
# time.sleep(2)
print("Hello after 2 sec")


# class custError(Exception):
#     pass


# raise custError("value is not correct")


class Website:
    def __init__(self, title):
        self.title = title

    def showTitle(self):
        print(self.title)


obj = Website('pythonbasics.org')
obj.showTitle()


class Plane:
    def __init__(self):
        self.wings = 2

        # fly
        self.drive()
        self.flaps()
        self.wheels()

    def drive(self):
        print('Accelerating')

    def flaps(self):
        print('Changing flaps')

    def wheels(self):
        print('Closing wheels')


ba = Plane()
