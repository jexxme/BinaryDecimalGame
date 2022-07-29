import random
import os
from unicodedata import decimal
import deco
import main
import time

def bin():
    reset_bin = True
    deco.message('Welcome to the Binary Converter!')
    print("\nYou will be asked to convert a decimal number to a binary number.")
    print("\nWhat difficulty do you want to play?\n")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print('\n4. Exit to Main Menu\n')
    
    try: 
        inp = int(input('Choose an option: '))
    except ValueError:
        print('\nPlease enter a number between 1 and 4!')
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        bin()

    if inp.__eq__(1):
        reset = False
        os.system('cls' if os.name == 'nt' else 'clear')
        binaryEasy()
    elif inp.__eq__(2):
        reset = False
        os.system('cls' if os.name == 'nt' else 'clear')
        binaryMedium()
    elif inp.__eq__(3):
        reset = False
        os.system('cls' if os.name == 'nt' else 'clear')
        binaryHard()
    elif inp.__eq__(4):
        reset = False
        print('Thanks for playing!')
        input("Press Enter to exit to main menu...")
        main.start()
    else:
        print('Invalid option!')
        input("Press Enter to continue...")
        reset = True
        os.system('cls' if os.name == 'nt' else 'clear')
        bin()

def binaryEasy():
    reset_bin = True
    score = 0
    while reset_bin:
        res = 0
        num = random.randrange(0, 3)

        print(f'Please convert the following decimal number to a binary:\n\n{num}\n')
        
        try:
            inp = int(input("My Answer:\n"))
        except ValueError:
            print('\nPlease enter a number!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
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
            deco.message2()
            time.sleep(1)
            continue
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
                binaryEasy()
            elif reset.__eq__(''):
                reset_bin = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                binaryEasy()
            else:
                reset = str(input('Do you want to exit to the main menu or change the difficulty level? <m/d>: '))
                if reset.__eq__('m'):
                    reset_bin = False
                    score = 0
        
                    input("Press Enter to exit to main menu...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main.start()
                elif reset.__eq__('d'):
                    reset_bin = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    bin()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_bin = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    bin()


def binaryMedium():
    reset_bin = True
    score = 0
    while reset_bin:
        res = 0
        num = random.randrange(0, 15)

        print(f'Please convert the following decimal number to a binary:\n\n{num}\n')
        
        try:
            inp = int(input("My Answer:\n"))
        except ValueError:
            print('\nPlease enter a number!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
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
            score += 2
            print(f'Curent Score: {score}')
            deco.message2()
            time.sleep(1)
            continue
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
                binaryMedium()
            elif reset.__eq__(''):
                reset_bin = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                binaryMedium()
            else:
                reset = str(input('Do you want to exit to the main menu or change the difficulty level? <m/d>: '))
                if reset.__eq__('m'):
                    reset_bin = False
                    score = 0
        
                    input("Press Enter to exit to main menu...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main.start()
                elif reset.__eq__('d'):
                    reset_bin = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    bin()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_bin = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    bin()


def binaryHard():
    reset_bin = True
    score = 0
    while reset_bin:
        res = 0
        num = random.randrange(7, 63)

        print(f'Please convert the following decimal number to a binary:\n\n{num}\n')
        
        try:
            inp = int(input("My Answer:\n"))
        except ValueError:
            print('\nPlease enter a number!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        if num / 64 >= 1:
           num -= 64
           res += 1000000
        if num / 32 >= 1:
           num -= 32
           res += 100000
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
            print('\nCorrect answer!')
            score += 3
            print(f'\nCurent Score: {score}')
            if score == 20:
                input(deco.endLevel())
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
                binaryHard()
            elif reset.__eq__(''):
                reset_bin = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                binaryHard()
            else:
                reset = str(input('Do you want to exit to the main menu or change the difficulty level? <m/d>: '))
                if reset.__eq__('m'):
                    reset_bin = False
                    score = 0
        
                    input("Press Enter to exit to main menu...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main.start()
                elif reset.__eq__('d'):
                    reset_bin = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    bin()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_bin = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    bin()