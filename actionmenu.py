# Course: CS 30:
# Period: 4
# Date created: 6/04/20
# Date last modified: 6/04/20
# Name: Maksim Sharoika
# Description: Game Test Program (Action Menu)
# The directions, actions and variables for the inputs.
directions = ["North", "East", "South", "West"]
actions = ["Shoot", "Heal", "Run"]
D = ()
A = ()


def choose_direction():
    # Choosing a direction function.
    global D
    D = input("Direction? ")
    if D in directions:
        print("----------")
        print(f"You will go {D}.")
        print("----------")
    else:
        print("----------")
        print("Invalid direction try again.")
        print("----------")
        choose_direction()


def choose_action():
    # Choosing an action function.
    global A
    A = input("Action? ")
    if A in actions:
        print("----------")
        print(f"You will {A}")
        print("----------")
    else:
        print("----------")
        print("Invalid action try again.")
        print("----------")
        choose_action()


def start_menu():
    # Starting the game function.
    print("Choose a direction to go in.")
    for direction in directions:
        print(f" > {direction}")
    choose_direction()
    print("Choose an action to perform.")
    for action in actions:
        print(f" > {action}")
    choose_action()
    end_menu()


def end_menu():
    # Ending the game function.
    print(f"You have decided to go {D} and {A}.")
    print("----------")

    def new_game():
        # Replaying / ending the game.
        G = input("Would you like to play again (Y/N)? ")
        if 'Y' in G:
            print("----------")
            start_menu()
        if 'N' in G:
            print("----------")
            print("Have a good day.")
        else:
            print("----------")
            print("Invalid action try again.")
            print("----------")
    new_game()
##########
# Calling start function.
start_menu()
##########
