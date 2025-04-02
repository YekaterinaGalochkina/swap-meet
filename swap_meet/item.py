import uuid #imported this to generate id

class Item:
    def __init__(self, id=None, condition=0):
        if id == None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition


    def get_category(self):
        return type(self).__name__ 
        

    def __str__(self): # overwrite default behavior of the built-in stringify
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        description = {
            0: "very bad condition",
            1: "bad condition",
            2: "fair condition",
            3: "okay condition",
            4: "almost new condition",
            5: "new condition"
        }
        if self.condition in description:  
            return description[self.condition]  



