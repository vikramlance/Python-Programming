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
