import deco
import main

def createLeaderboard():
    """
    Creates a leaderboard  file if it doesn't exist.
    """
    try:
        with open("Leaderboard.txt", "x") as f:
            f.write("")
        with open("Leaderboard.txt", "a") as f:
            f.write("Name : Gamemode : Score")
            f.write("\n")
            f.write("----------------------------------------------------")
    except FileExistsError:
        pass

def getLeaderboard():
    """
    Returns the leaderboard.
    """
    with open("leaderboard.txt", "r") as f:
        return f.read().split("\n")

def updateLeaderboard(name, gamemode, score):
    """
    Updates the leaderboard with the given name, gamemode, and score.
    """
    leaderboard = getLeaderboard()
    leaderboard.append(name + " : " + gamemode + " : " + str(score))
    with open("Leaderboard.txt", "w") as f:
        f.write("\n".join(leaderboard))

def resetLeaderboard():
    """
    Resets the leaderboard.
    """
    with open("Leaderboard.txt", "w") as f:
        f.write("Name : Gamemode : Score")
        f.write("\n")
        f.write("----------------------------------------------------")

# def sortLeaderboard(): # Not implemented yet
#     """
#     Sorts the leaderboard.
#     """
#     leaderboard = getLeaderboard()
#     leaderboard.sort(key=lambda x: int(x.split(":")[2]))
#     with open("leaderboard.txt", "w") as f:
#         f.write("\n".join(leaderboard))

def printLeaderboard():
    """
    Prints the leaderboard.
    """
    leaderboard = getLeaderboard()
    for i in range(len(leaderboard)):
        print(leaderboard[i])
    
    eingabe = str(input("\n\nDo you want to reset the leaderboard? (y/n) "))
    if eingabe == "y":
        resetLeaderboard()
        main.start()
    elif eingabe == "n":
        input("Press Enter to continue to the main menu...")
        main.start()
    else:
        main.start()