import random
import os
import deco
import binaryGame
import decimalGame


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
            binaryGame.bin()
        elif inp.__eq__(2):
            reset = False
            os.system('cls' if os.name == 'nt' else 'clear')
            decimalGame.dec()
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

if __name__ == '__main__':
    start()
