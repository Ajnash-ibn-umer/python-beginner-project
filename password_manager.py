import random

print('============  PASSWORD MANAGER ==============')

number=int(input('Enter number of passwords:'))

length=int(input('Enter password length: '))

char='qwertyuiopasdfghjklzxcvbnm1234567890-='

for x in range(number):
    pwd=''
    for c in range(length):
        pwd+=random.choice(char)
    

    print(pwd)
