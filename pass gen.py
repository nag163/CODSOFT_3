print('*'*80)
print("\t\t\t\t PASSWORD GENERATOR")
print('*'*80)
print(' Hi user!!   welcome to random password generator')
import random
import string

while(True):
    a=int(input('Do you want to generate password if yes press 1 else press 0 : '))
    if a==1:
        length = int(input("Enter the desired length of the password : "))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print("Generated Password:",   password)
    else:
        break
