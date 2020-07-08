import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

num_s = int(input('Enter the number of characters in password: '))
num_p = int(input('Enter the number of passwords: '))

for x in range(num_p):
    passw = ''

    for i in range(num_s):
        passw += random.choice(chars)

    print(passw)

    file = open('passw.txt', 'a')
    file.write('\n' + passw)
    file.close
