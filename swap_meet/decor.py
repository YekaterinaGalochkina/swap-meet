from .item import Item

class Decor(Item):
    def __init__(self, id=None, width=0, length=0, condition=0, age=0):
        super().__init__(id, condition, age)
        self.width = width
        self.length = length
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It takes up a {self.width} by {self.length} sized space."
    