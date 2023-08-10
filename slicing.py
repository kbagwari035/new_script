name = "Kul Bhushan"

#first_name = name[0:3]
first_name = name[:3]
#last_name = name[4:11]
last_name = name[4:]
#new_name = name[0:8:2]
new_name = name[::-1]


website = "http://google.com"
web = slice(7,-4)

print(name)
print(first_name)
print(last_name)
print(new_name)
print(website[web])
