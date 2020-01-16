# imports
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
   
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# create a player
# ask player for name
player = Player(input("what is your name? "), room['outside'])
print(player.current_room)

# allowed directions
directions = ["n", "s", "e", "w"]

# create a basic REPL 
while True:
    #read
    user = input(f"type: 'n' = north, 's' = south, 'e' = east , 'w' = west or 'q' to exit. \n {player.name} where would you like to go? ")
    # make sure user inputs n, s, e, w or q
    if user in directions:
        # player travels in inputed direction
        player.traveling(user)
    elif user == 'q':
        # quit game
        print('Thank you for playing, see you next time!')
        exit()
    else:
        print('command NOT allowed, please try again')