import string
import random
import os
os.system('cls')

def lower_build():
    lowercase_letters = string.ascii_lowercase
    return lowercase_letters

def upper_build():
    uppercase_letters = string.ascii_uppercase
    return uppercase_letters

def digit_build():
    digital_characters = string.digits
    return digital_characters

def symbol_build():
    symbols = """~!@#$%^&*-+{[]/\|_'"}"""
    return symbols

def space_build():
    space = ' '
    return space

def get_input(user_type):
    valid_answers = ['y','Y','Yes','YES','yes', 'n', 'N', 'No', 'NO', 'no']
    while True:
        user_input = input(f'\tDo you wish to use {user_type[0:-1]}? [y/n]'.ljust(50))
        while not (user_input in valid_answers):
            print('\t\tInvalid answer. Try again!')
            break        
        return user_input

def intro():
    print('\t _______________________________________________________________')
    print('\t|                                                               |')
    print('\t|     This is a program to generate a random password.          |')
    print('\t|     Valid characters for generating a password:               |')
    print('\t|        lowercase letters:        abcdefghijklmnopqrstuvwxyz   |')
    print('\t|        uppercase letters:        ABCDEFGHIJKLMNOPQRSTUVWXYZ   |')
    print('\t|        digital characters:       0123456789                   |')
    print('\t|        symbols:                  ~!@#$%^&*-+{[]/\|_\'\"}        |')
    print('\t|        space character:                                       |')
    print('\t|_______________________________________________________________|\n')

def password_generator():
    while True :
        try:
            n = int(input('\tEnter the length of password:'.ljust(50)))
        except ValueError:
            print('\t\tInvalid input. Try again!')          
        else:
            if n == 0:
                print('\t\tPassword\'s length cannot be zero! Try again!')
            elif n < 0:
                print('\t\tInvalid input. Try again!')
            else:
                break
    
    my_funcs = [['lowercase letters:', lower_build()], 
                ['uppercase letters:', upper_build()],
                ['digital characters:', digit_build()],
                ['symbols:', symbol_build()],
                ['space character:', space_build()]]   
       
    yes = ['y','Y','Yes','YES','yes']
    desired_characters = ''
    for element in my_funcs:
        if get_input(element[0]) in yes:
            desired_characters += element[1]

    if desired_characters == '':
        print('\n\t\tNo password generated! All of the above answers were NO.')
        return None
    else:
        password = ''
        for i in range(n):
            password += random.choice(desired_characters)
    print(75*'=')       
    return password

def run():
    intro()
    while True:
        created_pass = password_generator()
        if created_pass == None:
            print('\tTry again!')
        else:
            print(f'\tGenerated password is "{created_pass}".')
            print('\t _______________________________________________')
            print('\t|                                               |')
            print('\t|   Press Enter to repeat or any key to exit.   |')
            print('\t|_______________________________________________|')
            rep = input(' ')
            if rep != '':
                print('\t***********************END***********************\n')
                break

run()