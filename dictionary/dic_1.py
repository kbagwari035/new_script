# Dictionary is changeable, unordered collection of unique "key:value" pairs 
# Fast because they use hashing , allow us to access a value quickly

capitals = {"USA":"Washington",
            "INDIA":"New Delhi",
            "ENGLAND":"London",
            "CHINA":"Beijing"
            }

print(capitals.items())

print("Capital of USA is", capitals["USA"])
print("Capital of India is", capitals["INDIA"])
print("Capital of England is", capitals["ENGLAND"])
print("Capital of China is", capitals["CHINA"])

print("Capital of Germany is",capitals.get("GERMANY"))

capitals.update({"GERMANY":"Berlin"})

print(capitals.values())
print(capitals.keys())


    

