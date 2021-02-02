# Our simple list
game_list = [0,1,2]

# Displaying info
def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


# Getting user input info
def position_choice():

    # Initial choice
    choice = 'Error'

    # while choice is not a digit , keep asking for it
    while choice not in ['0','1','2']:

        choice = input("Pick a position (0,1,2): ")

        if choice not in ['0','1','2']:
            print("Sorry, invalid choice")
    return int(choice)

# Updating info
def replacement_choice(game_list,position):

    user_replacement = input("Type a string to place at position: ")

    game_list[position] = user_replacement

    return game_list


# Getting more user info
def gameon_choice():

    choice = 'Error'

    while choice not in ['Y','N','y','n']:

        choice = input("Keep playing ? (Y or N) ")

        if choice not in ['Y','N','y','n']:
            print("Sorry, I dont understand, please choose Y or N ")
    
    if choice == 'Y' or choice == 'y':
        return True
    elif choice == 'N' or choice == 'n':
        return False



gameon = True
game_list = [0,1,2]

while gameon:

    display_game(game_list)
    print('')
    position = position_choice()
    print('')
    game_list = replacement_choice(game_list,position)
    print('')
    display_game(game_list)
    print('')
    gameon =  gameon_choice()



