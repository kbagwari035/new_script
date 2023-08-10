"""
Scope --> The region that a variable is recognized a variable is only available from inside the region it is created. A global and locally scope versions of a variable can be created
"""

name = "Bhushan"      # global scope (available inside & outside function)
def display_name():
    name = "Kul"     #local scope (available only inside the function)
    print(name)

display_name()
print(name)
