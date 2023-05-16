# #passwordgenerator
import random 
import string
def generator_pw(min_length,number,special_character):
    letter=string.ascii_letters
    digit=string.digits
    special=string.punctuation
    character=letter

    if number:
        character+=digit
    if special_character:
        character+=special


    pwd=""
    meets_criteria=False
    has_number=False
    has_special=False
    while not meets_criteria or len(pwd)<min_length:
        new_char=random.choice(character)
        pwd+=new_char
        if new_char in digit:
            has_number=True
        if new_char in special:
            has_special=True
        meets_criteria=True
        if number:
            meets_criteria=has_number
        if special_character:
            meets_criteria=has_special
    return pwd
min_length=int(input("Enter the minimum length\n"))
has_number=input("Do you eant number(y/n)").lower()=='y'
has_special=input("Do you want special chatacter(y/n)").lower()=='y'
pwd=generator_pw(min_length,has_number,has_special)
print("The generated password is:", pwd)
