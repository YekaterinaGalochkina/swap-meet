import uuid #imported this to generate id

class Item:
    def __init__(self, id=None):
        if id == None:
            self.id = uuid.uuid4().int
        else:
            self.id = id


    def get_category(self):
        return type(self).__name__ 
        

    def __str__(self): # overwrite default behavior of the built-in stringify
        return f"An object of type {self.get_category()} with id {self.id}."
    


