import random
import os
import time
import deco
import main
import leaderboard

def decToBinary():
    reset_hex = True
    score = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    deco.message('Welcome to the Decimal to Binary Game!')
    print("\nChoose difficulty:\n")
    print("The higher the number, the harder the game.")
    print("But you will also get more points for each correct answer!\n")

    try:
        difficulty = int(input("Enter a number (16-256): \n\n"))
    except ValueError:
        print('\n\nPlease enter a number between 16 and 256!\n\n')
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        decToBinary()
    if difficulty < 16 or difficulty > 256:
        print("Please enter a number between 16 and 256!")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        decToBinary()
    os.system('cls' if os.name == 'nt' else 'clear')


    while reset_hex:
        randomInt = random.randint(16, difficulty)

        randomBin = bin(randomInt)

        res = randomBin[2:] # removes the 0b from the string
        
        res = int(res)

        print('Please convert the following Decimal number to a Binary:\n\n',randomInt,'\n')
        try:
            inp = input("My Answer:\n")
        except ValueError:
            print('\nPlease enter a number!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        if difficulty >= 16 and difficulty <= 85:
            points = 1
        elif difficulty >= 86 and difficulty <= 170:
            points = 2
        elif difficulty >= 171 and difficulty <= 256:
            points = 3

        if int(inp) == res:
            print('\nCorrect answer!')
            score += points
            print(f'\nCurrent Score: {score}\n')
            deco.message2()
            time.sleep(1)
            continue

        else:
            print('\nIncorrect answer!')
            print(f'Correct answer: {res}')
            print(f'Highscore: {score}\n')
            reset_hex = False

            if score > 0:
                saveScore = str(input("Do you want to save your score? (y/n)"))
                if saveScore.__eq__('y'):
                    name = input("Please enter your name: ")
                    leaderboard.updateLeaderboard(name, 'D->B', score)
                    print('\nYour score has been saved!')
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    decToBinary()

            reset = str(input('Do you want to play again? <y/n>: '))
            if reset.__eq__('y'):
                reset_hex= True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            elif reset.__eq__(''):
                reset_hex = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                decToBinary()
            else:
                reset = str(input('Do you want to exit to the main menu or change the difficulty level? <m/d>: '))
                if reset.__eq__('m'):
                    reset_hex = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main.start()
                elif reset.__eq__('d'):
                    reset_hex = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    decToBinary()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    decToBinary()
      

def binToDecimal():
    reset_hex = True
    score = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    deco.message('Welcome to the Binary to Decimal Game!')
    print("\nChoose difficulty:\n")
    print("The higher the number, the harder the game.")
    print("But you will also get more points for each correct answer!\n")

    try:
        difficulty = int(input("Enter a number (16-256): \n\n"))
    except ValueError:
        print('\n\nPlease enter a number between 16 and 256!\n\n')
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        binToDecimal()
    if difficulty < 16 or difficulty > 256:
        print("Please enter a number between 16 and 256!")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        binToDecimal()
    os.system('cls' if os.name == 'nt' else 'clear')


    while reset_hex:
        randomInt = random.randint(16, difficulty)

        randomBin = bin(randomInt)

        res = randomInt

        print('Please convert the following Binary number to a Decimal:\n\n',randomBin[2:],'\n')
        try:
            inp = input("My Answer:\n")
        except ValueError:
            print('\nPlease enter a number!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        if difficulty >= 16 and difficulty <= 85:
            points = 1
        elif difficulty >= 86 and difficulty <= 170:
            points = 2
        elif difficulty >= 171 and difficulty <= 256:
            points = 3

        if int(inp) == res:
            print('\nCorrect answer!')
            score += points
            print(f'\nCurrent Score: {score}\n')
            deco.message2()
            time.sleep(1)
            continue

        else:
            print('\nIncorrect answer!')
            print(f'Correct answer: {res}')
            print(f'Highscore: {score}\n')
            reset_hex = False

            if score > 0:
                saveScore = str(input("Do you want to save your score? (y/n)"))
                if saveScore.__eq__('y'):
                    name = input("Please enter your name: ")
                    leaderboard.updateLeaderboard(name, 'B->D', score)
                    print('\nYour score has been saved!')
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    binToDecimal()

            reset = str(input('Do you want to play again? <y/n>: '))
            if reset.__eq__('y'):
                reset_hex= True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            elif reset.__eq__(''):
                reset_hex = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                binToDecimal()
            else:
                reset = str(input('Do you want to exit to the main menu or change the difficulty level? <m/d>: '))
                if reset.__eq__('m'):
                    reset_hex = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main.start()
                elif reset.__eq__('d'):
                    reset_hex = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    binToDecimal()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    binToDecimal()
                    