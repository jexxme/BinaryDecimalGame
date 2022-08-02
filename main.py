import hexaGame
import os
import leaderboard
import random
import binDecGame
import octalGame


def start():
    leaderboard.createLeaderboard()
    reset = True
    while reset:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------------------------------")
        print('       Welcome to the Number System Game!')
        print("-----------------------------------------------------")
        print("\n       What Gamemode do you want to play?")
        print("-----------------------------------------------------")
        print("\n0. Random Gamemode\n")
        print('1. Decimal to Binary')
        print('2. Binary to Decimal')
        print("\n3. Hex to Binary")
        print("4. Binary to Hex")   
        print("\n5. Hex to Decimal")
        print("6. Decimal to Hex\n")
        print("\n7. Octal to Binary")
        print("8. Binary to Octal")
        print("-----------------------------------------------------")
        print('       9. View Leaderboard        10. Exit\n\n')
        
        try: 
            inp = int(input('Choose an option: '))
        except ValueError:
            print('\nPlease enter a number between 1 and 3!')
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if inp.__eq__(0):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            inp = random.randint(1,8)
        
        if inp.__eq__(1):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            binDecGame.decToBinary()
        elif inp.__eq__(2):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            binDecGame.binToDecimal()
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
            octalGame.octToBinary()
        elif inp.__eq__(8):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            octalGame.binToOctal()
        elif inp.__eq__(9):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            leaderboard.printLeaderboard()
        elif inp.__eq__(10):
            reset = False
            print('Thanks for playing!')
            print("Idea by: H.K.")
            print("Code by: Jerome")
            input("Press Enter to exit...")
            exit()
        else:
            print('Invalid option!')
            reset = True
            os.system('cls' if os.name == 'nt' else 'clear')
            start()

if __name__ == '__main__':
    start()
