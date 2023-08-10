"""
Nested function calls is functions calls inside other function calls inner most function calls are resolved first returned value is used as argument for the
next outer function
"""

"""
num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)
"""

num = round(abs(float(input("Enter a whole positive number: "))))
print(num)
