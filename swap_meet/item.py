import uuid 

class Item:
    def __init__(self, id=None, condition=0, age=0):
        if id == None:
            self.id = uuid.uuid4().int
        elif not isinstance(id, int):
            raise TypeError("id must be an integer")
        else:
            self.id = id
        if condition < 0 or condition > 5:
            raise ValueError("Condition must from 0 to 5")
        if age < 0:
            raise ValueError("Age must be a positive number")
        self.condition = condition
        self.age = age

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



