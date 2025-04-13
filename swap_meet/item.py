import uuid 

class Item:
    def __init__(self, id=None, condition=0, age=0):
        validate_item_data(id, condition, age) 

        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
        self.age = age

    def get_category(self):
        return self.__class__.__name__
        

    def __str__(self): 
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
            return description.get(self.condition, "unknown condition")  
        


#Helper function:

def validate_item_data(id, condition, age):
    if id is not None and not isinstance(id, int):
        raise TypeError("id must be an integer")
    
    if not isinstance(condition, (int, float)) or not (0 <= condition <= 5):
        raise ValueError("Condition must be a number from 0 to 5")

    if not isinstance(age, (int, float)) or age < 0:
        raise ValueError("Age must be a non-negative number")



