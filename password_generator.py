import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','+']

print("Welcome to the Python Password Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_numbers = int(input("How many numbers would you like in your password \n"))
nr_symbols = int(input("How many symbols would like in your password \n"))

# password = ""
# for char in range(1,nr_letters+1):
#     password += random.choice(letters)
# for char in range(1,nr_symbols+1):
#     password += random.choice(symbols)
# for char in range(1,nr_numbers+1):
#     password += random.choice(numbers)
#
# print(password)


#hard level
password_list = []
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password =""
for char in password_list:
    password += char
print(f" Your password is {password}")





