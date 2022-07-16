import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
rn=random.randint(0,len(names)-1)
sp=names[rn]
print(sp+" is going to buy the meal today!")