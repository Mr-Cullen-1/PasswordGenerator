# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:07:10 2024

@author: Jacob

Password Generator
"""

import string
import random

s1 = list(string.ascii_uppercase)
s2 = list(string.ascii_lowercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

user_input = input("Enter how many characters you would like to use in your password: ")

while True:
    try:    
        characters_number = int(user_input)
        if characters_number < 8 :
            print("Your number must be at least 8")
            user_input = input("Please, Enter your number again: ")
        else:
            break
    except:
        print("Please, enter numbers only!")
        user_input = input("Enter how many characters you would like to use in your password: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


part1 = round(characters_number * 30/100)
part2 = round(characters_number * 20/100)

result = []

for x in range(part1):
    
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    
    result.append(s3[x])
    result.append(s4[x])

random.shuffle(result)

password = "".join(result)
print("Strong password: ", password)