import random

#variables
uID="" #variable to store the password
#variables from which random characters will be taken
alpha=["#","@","!","$","%","^","&","*"]
num=["1","2","3","4","5","6","7","8","9","0"]
char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#to create random password
for i in range(4):
    uID=uID+random.choice(num)+random.choice(alpha)+random.choice(char)

print(uID) #password
print(len(uID)) #password length
