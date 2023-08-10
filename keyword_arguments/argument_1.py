"""
Keyword arguments  is argument preceded by an identifier when we pass them to a function 
The order of the arguments doesn't matter, unlike positional arguments
Python knows the names of the arguments that our function receives
"""

def hello(first,middle,last):
    print("Hello"+" "+middle+" "+last)
hello(middle="Bhushan",last="Bagwari",first="Kul")
