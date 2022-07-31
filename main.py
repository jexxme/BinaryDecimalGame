import hexaGame
import os
import deco
import binaryGame
import decimalGame
import leaderboard

def start():
    leaderboard.createLeaderboard()
    reset = True
    while reset:
        os.system('cls' if os.name == 'nt' else 'clear')
        deco.message('Welcome to the Number System Game!')
        print("\nWhat gamemode do you want to play?\n")
        print('1. Decimal to Binary')
        print('2. Binary to Decimal')
        print("\n3. Hex to Binary")
        print("4. Binary to Hex")   
        print("\n5. Hex to Decimal")
        print("6. Decimal to Hex\n")
        deco.message3()
        print('    7. View Leaderboard       8. Exit\n\n')
        
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
            binaryGame.bin()
        elif inp.__eq__(2):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            decimalGame.dec()
        elif inp.__eq__(3):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            hexaGame.hexToBinary()
        elif inp.__eq__(4):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            hexaGame.binToHexadecimal()
        elif inp.__eq__(5):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            hexaGame.hexToDecimal()
        elif inp.__eq__(6):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            hexaGame.binToHexadecimal()
        elif inp.__eq__(7):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            leaderboard.printLeaderboard()
        elif inp.__eq__(8):
            reset = False
            print('Thanks for playing!')
            print("Idea by: H.K.")
            print("Code by: Jerome and H.K.")
            input("Press Enter to exit...")
            exit()
        else:
            print('Invalid option!')
            reset = True
            os.system('cls' if os.name == 'nt' else 'clear')
            start()

if __name__ == '__main__':
    start()
