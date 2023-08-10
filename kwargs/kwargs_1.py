"""
kwargs is parameter that will pick all arguments into a dictionary useful so 
that a function can accept a varying amount of keyword argument

"""

def hello(**kwargs):
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
hello(title="Mr.",first="Kul",middle="Bhushan",last="Bagwari")
