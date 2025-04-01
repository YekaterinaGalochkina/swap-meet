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
    
    def get_by_id(self, item_id): 
        for item in self.inventory:
            if item_id == item.id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True
    
    # Wave 4
    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        first_item_vendor = self.inventory[0]
        first_item_friends = other_vendor.inventory[0]
        self.inventory.remove(first_item_vendor)
        self.inventory.append(first_item_friends)
        other_vendor.inventory.remove(first_item_friends)
        other_vendor.inventory.append(first_item_vendor)
        return True

    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.get_category() == category:
                category_items.append(item)
        return category_items

    def get_best_by_category(self, category): # review this
        best_item = None
        for item in self.inventory:
            if item.get_category() == category:
                if not best_item or item.condition > best_item.condition:
                    best_item = item
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if their_priority.get_category() == self.inventory.get_category():
            

