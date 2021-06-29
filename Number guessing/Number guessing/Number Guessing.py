import random

system_guessed=random.randint(0,100)
print("System has generated a random number")

while True:
    try:
        user_guessed=int(input("Guess the number : "))
    except:
        print('''"""\nPlease enter a valid numeric input\n""" ''')
        continue

    if(user_guessed == system_guessed):
        print("Congratulations !!...\nYou got it.")
        break
    elif(user_guessed > system_guessed):
        print("Sorry...\nBut it's smaller than this number.")
    elif(user_guessed < system_guessed):
        print("Sorry...\nBut it's bigger than this number.")
    else:
        print("Something went wrong, invalid input")




