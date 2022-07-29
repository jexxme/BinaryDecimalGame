import random
import os
import deco

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
