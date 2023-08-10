food = ["pizza", "burger", "hotdog", "sandwich"]
print(food)

print(food[1])
print(type(food))

food.append("salad")
print(food)

food.insert(0,"newitem")
print(food)

food.remove("newitem")
print(food)

food.pop(4)
print(food)

food.sort()
for i in food:
    print(i)

food.clear()
print(food)
