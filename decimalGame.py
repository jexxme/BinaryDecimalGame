import random
import os
from unicodedata import decimal
import deco
import main
import time
import leaderboard

def dec():
    reset_dec = True
    deco.message('Welcome to the Binary to Decimal Game!')
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

    if inp.__eq__(1):
        reset = False
        os.system('cls' if os.name == 'nt' else 'clear')
        decimalEasy()
    elif inp.__eq__(2):
        reset = False
        os.system('cls' if os.name == 'nt' else 'clear')
        decimalMedium()
    elif inp.__eq__(3):
        reset = False
        os.system('cls' if os.name == 'nt' else 'clear')
        decimalHard()
    elif inp.__eq__(4):
        reset = False
        main.start()
    else:
        print('Invalid option!')
        input("Press Enter to continue...")
        reset = True
        os.system('cls' if os.name == 'nt' else 'clear')
        dec()


    

def decimalEasy():
    reset_dec = True
    score = 0
    while reset_dec:
        ones = random.randrange(0, 2)
        tens = random.randrange(0, 2)
        huns = random.randrange(0, 2)

        res = 0
        num = f'{huns}{tens}{ones}'

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

        if inp.__eq__(res):
            print('\nCorrect answer!')
            score += 1
            print(f'\nCurrent Score: {score}\n')
            deco.message2()
            time.sleep(1)
            continue

        else:
            print('\nIncorrect answer!')
            print(f'Correct answer: {res}')
            print(f'Highscore: {score}\n')
            reset_dec = False

            if score > 0:
                saveScore = str(input("Do you want to save your score? (y/n)"))
                if saveScore.__eq__('y'):
                    name = input("Please enter your name: ")
                    leaderboard.updateLeaderboard(name, 'B->D', score)
                    print('\nYour score has been saved!')
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dec()

            reset = str(input('Do you want to play again? <y/n>: '))
            if reset.__eq__('y'):
                reset_dec = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                decimalEasy()
            elif reset.__eq__(''):
                reset_dec = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                decimalEasy()
            else:
                reset = str(input('Do you want to exit to the main menu or change the difficulty level? <m/d>: '))
                if reset.__eq__('m'):
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main.start()
                elif reset.__eq__('d'):
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dec()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dec()
                    

def decimalMedium():
    score = 0
    reset_dec = True
    while reset_dec:
        ones = random.randrange(0, 2)
        tens = random.randrange(0, 2)
        huns = random.randrange(0, 2)
        tous = random.randrange(0, 2)
        tets = random.randrange(0, 2)

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

        if inp.__eq__(res):
            print('\nCorrect answer!')
            score += 2
            print(f'Current Score: {score}\n')
            deco.message2()
            time.sleep(1)
            continue

        else:
            print('\nIncorrect answer!')
            print(f'Correct answer: {res}')
            print(f'Highscore: {score}\n')

            if score > 0:
                saveScore = str(input("Do you want to save your score? (y/n)"))
                if saveScore.__eq__('y'):
                    name = input("Please enter your name: ")
                    leaderboard.updateLeaderboard(name, 'B->D', score)
                    print('\nYour score has been saved!')
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dec()

            reset_dec = False
            reset = str(input('Do you want to play again? <y/n>: '))
            if reset.__eq__('y'):
                reset_dec = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                decimalEasy()
            elif reset.__eq__(''):
                reset_dec = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                decimalEasy()
            else:
                reset = str(input('Do you want to exit to the main menu or change the difficulty level? <m/d>: '))
                if reset.__eq__('m'):
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main.start()
                elif reset.__eq__('d'):
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dec()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dec()
                    

def decimalHard():
    score = 0
    reset_dec = True
    while reset_dec:
        ones = random.randrange(0, 2)
        tens = random.randrange(0, 2)
        huns = random.randrange(0, 2)
        tous = random.randrange(0, 2)
        tets = random.randrange(0, 2)
        huts = random.randrange(0, 2)
        mils = random.randrange(0, 2)

        res = 0
        num = f'{mils}{huts}{tets}{tous}{huns}{tens}{ones}'

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
        if huts.__eq__(1):
             res += 32
        if mils.__eq__(1):
             res += 64

        if inp.__eq__(res):
            print('\nCorrect answer!')
            score += 3
            print(f'Current Score: {score}\n')
            deco.message2()
            time.sleep(1)
            continue

        else:
            print('\nIncorrect answer!')
            print(f'Correct answer: {res}')
            print(f'Highscore: {score}\n')

            if score > 0:
                saveScore = str(input("Do you want to save your score? (y/n)"))
                if saveScore.__eq__('y'):
                    name = input("Please enter your name: ")
                    leaderboard.updateLeaderboard(name, 'B->D', score)
                    print('\nYour score has been saved!')
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dec()

            reset_dec = False
            reset = str(input('Do you want to play again? <y/n>: '))
            if reset.__eq__('y'):
                reset_dec = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                decimalEasy()
            elif reset.__eq__(''):
                reset_dec = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                decimalEasy()
            else:
                reset = str(input('Do you want to exit to the main menu or change the difficulty level? <m/d>: '))
                if reset.__eq__('m'):
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main.start()
                elif reset.__eq__('d'):
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dec()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dec()
                    