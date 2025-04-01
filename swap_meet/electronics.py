import uuid 

class Electronics:
    def __init__(self, id=None, type="Unknown", condition=0):
        if id == None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.type = type
        self.condition = condition

    def get_category(self):
        return type(self).__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. This is a {self.type} device."
    
    def condition_description(self):
        description = {
            0: "very bad condition",
            1: "bad condition",
            2: "fair condition",
            3: "okay condition",
            4: "almost new condition",
            5: "new condition"
        }
        for key, value in description.items():
            if self.condition == key:
                return value