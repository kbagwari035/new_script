# set = collections which is unordered, unindexed and no duplicate values
# Joing two sets in new set

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup"}

dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)

