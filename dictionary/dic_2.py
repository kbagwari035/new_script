# Dictionary is changeable, unordered collection of unique "key:value" pairs 
# Fast because they use hashing , allow us to access a value quickly

capitals = {"USA":"Washington",
            "INDIA":"New Delhi",
            "ENGLAND":"London",
            "CHINA":"Beijing"
            }

for i in capitals.keys():
    print(i)

for i in capitals.values():
    print(i)

for key,value in capitals.items():
    print(key,value)

