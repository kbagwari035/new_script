# set = collections which is unordered, unindexed and no duplicate values

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup"}

print(utensils)
print(dishes)

utensils.update(dishes)

for x in utensils:
    print(x)

