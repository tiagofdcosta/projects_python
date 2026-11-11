import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Automatic Password Generator!")

password = ""
password_list = []

for char in range(0, 10):
    password_list.append(random.choice(letters))

for char in range(0, 5):
    password_list.append(random.choice(symbols))

for char in range(0, 5):
    password_list.append(random.choice(numbers))

# print(password_list)
random.shuffle(password_list)
#print("Shuffle Paswword: ", password_list)

# switch from list to table
for char in password_list:
    password = password + char

print(f"Your password is:  {password}")

