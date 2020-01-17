# item class
class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        string = f"items: {self.name}, {self.description}"
        return string

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")