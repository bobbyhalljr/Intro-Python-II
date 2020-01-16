# player class
class Player:

    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []

    def traveling(self, direction):
        # player can move in a direction
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print('That direction is not allowed, pick another direction')
