import string
import random as r

s1=list(string.ascii_uppercase)
s2=list(string.ascii_lowercase)
s3=list(string.digits)
s4=list(string.punctuation)

char_num=input('write the number of characters of your password :')

while True:
    try:
        char_num=int(char_num)
        if char_num < 6 :
            print('ERROR! THE LEAST PASSWORD CONSISTS OF 6 CHARACTERS')
            char_num=input('write the number of characters of your password :')
        else:
            break
    except:
        print('please enter numbers only')
        char_num=input('write the number of characters of your password :')

r.shuffle(s1)
r.shuffle(s2)
r.shuffle(s3)
r.shuffle(s4)

part1=round(char_num*(30/100))
part2=round(char_num*(20/100))

#print(part1,part2)
password= []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])
for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

r.shuffle(password)

password="".join(password[:])
print("your random generated password is ",password)