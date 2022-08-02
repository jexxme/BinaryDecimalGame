import random
import os
import time
import deco
import main
import leaderboard

def octToBinary():
    reset_oct = True
    score = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    deco.message('Welcome to the Octal to Binary Game!')
    print("\nChoose difficulty:\n")
    print("The higher the number, the harder the game.")
    print("But you will also get more points for each correct answer!\n")

    try:
        difficulty = int(input("Enter a number (16-256): \n\n"))
    except ValueError:
        print('\n\nPlease enter a number between 16 and 256!\n\n')
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        octToBinary()
    if difficulty < 16 or difficulty > 256:
        print("Please enter a number between 16 and 256!")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        octToBinary()
    os.system('cls' if os.name == 'nt' else 'clear')
        
    while reset_oct:
        randomInt = random.randint(0,difficulty)
        randomOct = oct(randomInt)[2:]
        randomBin = bin(randomInt)[2:]
        res = randomBin

        print(f'Please convert the following Octal number to a binary number:\n\n' + randomOct + '\n')
        try:
            inp = str(input("My Answer:\n"))
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

        if inp == res:
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
            reset_oct = False

            if score > 0:
                saveScore = str(input("Do you want to save your score? (y/n)"))
                if saveScore.__eq__('y'):
                    name = input("Please enter your name: ")
                    leaderboard.updateLeaderboard(name, 'O->B', score)
                    print('\nYour score has been saved!')
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    octToBinary()

            reset = str(input('Do you want to play again? <y/n>: '))
            if reset.__eq__('y'):
                reset_oct= True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            elif reset.__eq__(''):
                reset_oct = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                octToBinary()
            else:
                reset = str(input('Do you want to exit to the main menu or change the difficulty level? <m/d>: '))
                if reset.__eq__('m'):
                    reset_oct = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main.start()
                elif reset.__eq__('d'):
                    reset_oct = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    octToBinary()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    octToBinary()


def binToOctal():
    reset_oct = True
    score = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    deco.message('Welcome to the Binary to Octal Game!')
    print("\nChoose difficulty:\n")
    print("The higher the number, the harder the game.")
    print("But you will also get more points for each correct answer!\n")

    try:
        difficulty = int(input("Enter a number (16-256): \n\n"))
    except ValueError:
        print('\n\nPlease enter a number between 16 and 256!\n\n')
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        binToOctal()
    if difficulty < 16 or difficulty > 256:
        print("Please enter a number between 16 and 256!")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        binToOctal()
    os.system('cls' if os.name == 'nt' else 'clear')
        
    while reset_oct:
        randomInt = random.randint(0,difficulty)
        randomOct = oct(randomInt)[2:]
        randomBin = bin(randomInt)[2:]
        res = randomOct

        print(f'Please convert the following Binary number to a Octal number:\n\n' + randomBin + '\n')
        try:
            inp = str(input("My Answer:\n"))
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

        if inp == res:
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
            reset_oct = False

            if score > 0:
                saveScore = str(input("Do you want to save your score? (y/n)"))
                if saveScore.__eq__('y'):
                    name = input("Please enter your name: ")
                    leaderboard.updateLeaderboard(name, 'B->O', score)
                    print('\nYour score has been saved!')
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    binToOctal()

            reset = str(input('Do you want to play again? <y/n>: '))
            if reset.__eq__('y'):
                reset_oct= True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            elif reset.__eq__(''):
                reset_oct = True
                score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                binToOctal()
            else:
                reset = str(input('Do you want to exit to the main menu or change the difficulty level? <m/d>: '))
                if reset.__eq__('m'):
                    reset_oct = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main.start()
                elif reset.__eq__('d'):
                    reset_oct = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    binToOctal()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_oct = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    binToOctal()