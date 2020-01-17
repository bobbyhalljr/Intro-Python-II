# room class
class Room:

    def __init__(self, name, description):
        # name and description
        self.name = name
        self.description = description
        # n_to, s_to, e_to, w_to
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        string = ''
        string += f"\n*****************\n"
        string += f"\n{self.name}\n"
        string += f"\n{self.description}\n" 
        string += f"\n The items in the room are: {self.items}\n" 
        string += f"\n{self.get_exit_string()}\n" 
        return string

    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None

    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

    def get_exit_string(self):
        return f"Exits: {','.join(self.get_exits())}"
