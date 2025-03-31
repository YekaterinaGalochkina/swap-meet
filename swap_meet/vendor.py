from swap_meet.item import Item #imported item

class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_id(self, item_id): #added this method
        for item in self.inventory:
            if item_id == item.id:
                return item
        return None