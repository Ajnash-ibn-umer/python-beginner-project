import random

print('============  PASSWORD MANAGER ==============')

number=int(input('Enter number of passwords:'))

length=int(input('Enter password length: '))

char='qwertyuiop[]asdfghjkl;\zxcvbnm,./<>?:|}{1234567890-=!@#$%^&*()_+`~'

for x in range(number):
    pwd=''
    for c in range(length):
        pwd+=random.choice(char)
    

    print(pwd)
