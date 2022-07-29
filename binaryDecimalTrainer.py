import random
import os
import deco


#TODO menu to choose difficulty level (easy, medium, hard) 
#Könnte man mit mehreren pythonfiles realisieren
#Bspw. ein file mit start()
#ein weiteres file für dec() (mit 3 Funktionen, leicht,mittel,schwer)
#ein weiteres file für bin() (mit 3 Funktionen, leicht,mittel,schwer)
#bin und dec werden dann mit start() aufgerufen und die Funktionen werden ausgeführt


def start():
    reset = True
    while reset:
        deco.message('Welcome to the Binary/Decimal Converter!')
        print("\nWhat gamemode do you want to play?\n")
        print('1. Binary to Decimal')
        print('2. Decimal to Binary')
        print('\n3. Exit\n')
        
        try: 
            inp = int(input('Choose an option: '))
        except ValueError:
            print('\nPlease enter a number between 1 and 3!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if inp.__eq__(1):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            bin()
        elif inp.__eq__(2):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            dec()
        elif inp.__eq__(3):
            reset = False
            print('Thanks for playing!')
            input("Press Enter to exit...")
            exit()
        else:
            print('Invalid option!')
            reset = True
            os.system('cls' if os.name == 'nt' else 'clear')
            start()

def bin():
    reset_bin = True
    score = 0
    while reset_bin:
        res = 0
        num = random.randrange(0, 31)

        print(f'Please convert the following decimal number to a binary:\n\n{num}\n')
        
        try:
            inp = int(input("My Answer:\n"))
        except ValueError:
            print('\nPlease enter a number!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        #if num / 64 >= 1:
        #    num -= 64
        #    res += 1000000
        #if num / 32 >= 1:
        #    num -= 32
        #    res += 100000
        if num / 16 >= 1:
            num -= 16
            res += 10000
        if num / 8 >= 1:
            num -= 8
            res += 1000
        if num / 4 >= 1:
            num -= 4
            res += 100
        if num / 2 >= 1:
            num -= 2
            res += 10
        if num / 1 == 1:
            num -= 1
            res += 1

        if inp.__eq__(res):
            print('Correct answer!')
            score += 1
            print(f'Curent Score: {score}')
            print()
        else:
            print(f'Incorrect answer!')
            print(f'Correct answer: {res}')
            print()
            print(f'Highscore: {score}')
            reset_bin = False

            reset = str(input('Do you want to play again? <y/n>: '))
            if reset.__eq__('y'):
                reset_bin = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                bin()
            else:
                reset_bin = False
                score = 0
                print('Thanks for playing!')
                input("Press Enter to exit...")
                exit()

def dec():

    reset_dec = True
    score = 0

    while reset_dec:

        ones = random.randrange(0, 2)
        tens = random.randrange(0, 2)
        huns = random.randrange(0, 2)
        tous = random.randrange(0, 2)
        tets = random.randrange(0, 2)
        huts = random.randrange(0, 2)
        mils = random.randrange(0, 2)

        res = 0
        num = f'{tets}{tous}{huns}{tens}{ones}'

        print(f'Please convert the following binary number to a decimal:\n\n{num}\n')

        try:
            inp = int(input("My Answer:\n"))
        except ValueError:
            print('\nPlease enter a number!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if ones.__eq__(1):
            res += 1
        if tens.__eq__(1):
            res += 2
        if huns.__eq__(1):
            res += 4
        if tous.__eq__(1):
            res += 8
        if tets.__eq__(1):
             res += 16
        # if huts.__eq__(1):
        #      res += 32
        # if mils.__eq__(1):
        #      res += 64

        if inp.__eq__(res):
            print('\nCorrect answer!')
            score += 1
            print(f'Current Score: {score}\n')

        else:
            print('\nIncorrect answer!')
            print(f'Correct answer: {res}')
            print(f'Highscore: {score}\n')
            reset_dec = False

            reset = str(input('Do you want to play again? <y/n>: '))
            if reset.__eq__('y'):
                reset_dec = True
                reset_bin = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                dec()
            else:
                reset_dec = False
                reset_bin = False
                score = 0
                print('Thanks for playing!')
                input("Press Enter to exit...")
                exit()

if __name__ == '__main__':
    start()
