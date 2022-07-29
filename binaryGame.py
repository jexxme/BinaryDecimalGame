import random
import os
import deco

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