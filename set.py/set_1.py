# set = collections which is unordered, unindexed and no duplicate values

utensils = {"fork", "spoon", "knife"}
print(utensils)

utensils.add("napkin")
print(utensils)

for x in utensils:
    print(x)

utensils.remove("napkin")
print(utensils)

utensils.clear()
print(utensils)
