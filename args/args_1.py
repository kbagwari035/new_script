"""
args : is parameter that will pack all arguments into a tuple useful so that a 
function can accept a varying amount of arguments
"""
"""
def add(num_1,num_2):
    sum = num_1 + num_2
    return sum
print(add(1,2))

"""

def add(*args):
    sum = 0
    #stuff = list(stuff)
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6,))

def add(*test):
    sum = 0
    test = list(test)
    test[0] = 0
    for i in test:
        sum += i
    return sum

print(add(1,2,3,4,5,6,))

