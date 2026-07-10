#this program generate the password by randomly selecting characters from a predefined set of characters and using only for loops and range and random module. The program prompts the user to enter the desired length of the password and then generates a random password of that length. The generated password is printed to the console.


import random
letters = [
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
          ]
          
          
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', 
    "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|', 
    '`', '~'
] 

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))
password = ""
for i in range(n_letters):
    password+=random.choice(letters)

for i in range(n_symbols):
    password+=random.choice(symbols)

for i in range(n_numbers):
    password+=random.choice(numbers)

print("your password is = ", password)