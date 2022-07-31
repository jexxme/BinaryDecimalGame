import random
import os
import time
from tkinter.messagebox import QUESTION
import deco
import main
import leaderboard

def hexToBinary():
    reset_hex = True
    score = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    deco.message('Welcome to the Hexadecimal to Binary Converter!')
    print("\nChoose difficulty:\n")
    print("The higher the number, the harder the game.")
    print("But you will also get more points for each correct answer!\n")

    try:
        diff = int(input("Enter a number (16-256): \n\n"))
    except ValueError:
        print('\n\nPlease enter a number between 16 and 256!\n\n')
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        hexToBinary()
    if diff < 16 or diff > 256:
        print("Please enter a number between 16 and 256!")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        hexToBinary()
    os.system('cls' if os.name == 'nt' else 'clear')

    def binToHex(n):
        num = int(n, 2)
        hex_num = format(num, 'x')
        return(hex_num)

    def hexToBin(n):
        num = int(n, 16)
        bin_num = format(num, 'b')
        return(bin_num)
        
    while reset_hex:
        randomInt = random.randint(0,diff)
        randomHexa = hex(randomInt)[2:]
        res = hexToBin(randomHexa)
        print(f'Please convert the following hexadecimal number to a binary:\n\n' + randomHexa + '\n')
        try:
            inp = str(input("My Answer:\n"))
        except ValueError:
            print('\nPlease enter a number!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if inp == res:
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
            reset_hex = False

            if score > 0:
                saveScore = str(input("Do you want to save your score? (y/n)"))
                if saveScore.__eq__('y'):
                    name = input("Please enter your name: ")
                    leaderboard.updateLeaderboard(name, 'H->B', score)
                    print('\nYour score has been saved!')
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    hexToBinary()

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
                hexToBinary()
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
                    hexToBinary()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    hexToBinary()
                    
#mehr punkte durch for loop der variable erhöht graduelle und iteration ist eingabe von user
def binToHexadecimal():
    reset_hex = True
    score = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    deco.message('Welcome to the Binary to Hexadecimal Converter!')
    print("\nChoose difficulty:\n")
    print("The higher the number, the harder the game.")
    print("But you will also get more points for each correct answer!\n")
    
    try:
        diff = int(input("Enter a number (16-256): \n\n"))
    except ValueError:
        print('\n\nPlease enter a number between 16 and 256!\n\n')
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        binToHexadecimal()
    if diff < 16 or diff > 256:
        print("Please enter a number between 16 and 256!")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        binToHexadecimal()
    os.system('cls' if os.name == 'nt' else 'clear')

    while reset_hex:
        def binToHex(n): #braucht bin string als input und gibt hex string zurück
            # convert binary to int
            num = int(n, 2)
            # convert int to hexadecimal
            hex_num = hex(num)
            return(hex_num)

        randomInt = int(random.randint(0,diff)) #create random number, diff is the difficulty set by the user
        randomBin = bin(randomInt)[2:] #convert to binary
        randomHex = binToHex(randomBin)[2:] #convert to hexadecimal
        res = randomHex #save the random hexadecimal number

        print(f'Please convert the following Binary number to a Hexadecimal:\n\n' + randomBin + '\n')
        try:
            inp = str(input("My Answer:\n"))
        except ValueError:
            print('\nPlease enter a number!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if inp == res:
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
            reset_hex = False

            if score > 0:
                saveScore = str(input("Do you want to save your score? (y/n)"))
                if saveScore.__eq__('y'):
                    name = input("Please enter your name: ")
                    leaderboard.updateLeaderboard(name, 'H->B', score)
                    print('\nYour score has been saved!')
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')
            
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
                continue
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
                    binToHexadecimal()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_dec = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    binToHexadecimal()
                    
def hexToDecimal():
    reset_hex = True
    score = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    deco.message('Welcome to the Hexadecimal to Decimal Converter!') # sehr random bug:AttributeError: partially initialized module 'deco' has no attribute 'message' (most likely due to a circular import)
    print("\nChoose difficulty:\n")
    print("The higher the number, the harder the game.")
    print("But you will also get more points for each correct answer!\n")
    
    try:
        diff = int(input("Enter a number (16-256): \n\n"))
    except ValueError:
        print('\n\nPlease enter a number between 16 and 256!\n\n')
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        hexToDecimal()
    if diff < 16 or diff > 256:
        print("Please enter a number between 16 and 256!")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        hexToDecimal()
    os.system('cls' if os.name == 'nt' else 'clear')

    while reset_hex:
        def binToHex(n): #braucht bin string als input und gibt hex string zurück
            # convert binary to int
            num = int(n, 2)
            # convert int to hexadecimal
            hex_num = hex(num)
            return(hex_num)

        randomInt = int(random.randint(0,diff)) #create random number, diff is the difficulty set by the user
        randomBin = bin(randomInt)[2:] #convert to binary
        randomHex = binToHex(randomBin)#convert to hexadecimal
        res = int(randomHex, base=16) #save the random hexadecimal number as result 

        print(f'Please convert the following Hexadecimal number to a Decimal:\n\n' + randomHex[2:] + '\n')
        try:
            inp = str(input("My Answer:\n"))
        except ValueError:
            print('\nPlease enter a number!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if inp == str(res):
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
            reset_hex = False

            if score > 0:
                saveScore = str(input("Do you want to save your score? (y/n)"))
                if saveScore.__eq__('y'):
                    name = input("Please enter your name: ")
                    leaderboard.updateLeaderboard(name, 'H->D', score)
                    print('\nYour score has been saved!')
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')
            
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
                continue
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
                    hexToDecimal()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_hex = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    hexToDecimal()

def decToHexadecimal():
    reset_hex = True
    score = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    deco.message('Welcome to the Decimal to Hexadecimal Converter!') 
    print("\nChoose difficulty:\n")
    print("The higher the number, the harder the game.")
    print("But you will also get more points for each correct answer!\n")
    
    try:
        diff = int(input("Enter a number (16-256): \n\n"))
    except ValueError:
        print('\n\nPlease enter a number between 16 and 256!\n\n')
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        decToHexadecimal()
    if diff < 16 or diff > 256:
        print("Please enter a number between 16 and 256!")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        decToHexadecimal()
    os.system('cls' if os.name == 'nt' else 'clear')

    while reset_hex:
        def binToHex(n): #braucht bin string als input und gibt hex string zurück
            # convert binary to int
            num = int(n, 2)
            # convert int to hexadecimal
            hex_num = hex(num)
            return(hex_num)
        randomInt = int(random.randint(0,diff)) #create random number, diff is the difficulty set by the user
        randomBin = bin(randomInt)[2:] #convert to binary
        randomHex = binToHex(randomBin)#convert to hexadecimal
        question = str(randomInt)
        res = randomHex[2:] #save the random hexadecimal number as result withot the 0x prefix

        print(f'Please convert the following Decimal number to a Hexadecimal:\n\n' + question + '\n')
        try:
            inp = str(input("My Answer:\n"))
        except ValueError:
            print('\nPlease enter a number!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if inp == str(res):
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
            reset_hex = False

            if score > 0:
                saveScore = str(input("Do you want to save your score? (y/n)"))
                if saveScore.__eq__('y'):
                    name = input("Please enter your name: ")
                    leaderboard.updateLeaderboard(name, 'D->H', score)
                    print('\nYour score has been saved!')
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')
            
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
                continue
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
                    decToHexadecimal()
                else:
                    print('Invalid option!')
                    input("Press Enter to continue...")
                    reset_hex = False
                    score = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    decToHexadecimal()