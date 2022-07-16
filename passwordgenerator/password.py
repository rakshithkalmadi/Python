#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nrl= int(input("How many letters would you like in your password?\n")) 
nrs = int(input(f"How many symbols would you like?\n"))
nrn = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
sudo=""
for i in range(0,int(nrl)+1):
  ranlet=letters[int(random.randint(0,int(len(letters))-1))]
  sudo+=ranlet

for i in range(0,int(nrs)+1):
  ranspe=symbols[int(random.randint(0,int(len(symbols))-1))]
  sudo+=ranspe
for i in range(0,int(nrn)+1):
  rannum=numbers[int(random.randint(0,int(len(numbers))-1))]
  sudo+=rannum
print("Non shufelled password")
print(sudo)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
out=''.join(random.sample(sudo,len(sudo)))
#outt=random.shuffle(sudo) it is for the array
print("Shufelled password")
print(out)
#print(outt)