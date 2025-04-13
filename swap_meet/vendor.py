from swap_meet.item import Item 

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
        new_inventory = []

        for piece in self.inventory:
            if piece != item:
                new_inventory.append(piece)
        
        if len(new_inventory) == len(self.inventory):
            return False
        
        self.inventory = new_inventory
        return item
    
    def get_by_id(self, item_id): 
        for item in self.inventory:
            if item_id == item.id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        if not self.remove(my_item):
            return False
        if not other_vendor.remove(their_item):
            self.add(my_item)
            return False

        self.add(their_item)
        other_vendor.add(my_item)
        return True
    
    # Wave 4
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
            
        first_item_vendor = self.inventory[0]
        first_item_friends = other_vendor.inventory[0]
        
        return self.swap_items(other_vendor, first_item_vendor, first_item_friends)

    def get_by_category(self, category):
        category_items = []

        for item in self.inventory:
            if item.get_category() == category:
                category_items.append(item)

        return category_items

    def get_best_by_category(self, category): 
        best_condition = -1
        best_item = None

        for item in self.inventory:
            if item.get_category() == category and item.condition > best_condition:
                best_condition = item.condition
                best_item = item

        return best_item
    
    
    def swap_by_newest(self, other_vendor):
        my_newest_item = self.get_newest_item()
        their_newest_item = other_vendor.get_newest_item()

        if my_newest_item and their_newest_item:
            return self.swap_items(other_vendor, my_newest_item, their_newest_item)
    
        return False
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        
        if not my_best_item or not their_best_item:
            return False
        
        if my_best_item and their_best_item:
            return self.swap_items(other_vendor, my_best_item, their_best_item)
        

    # Helper function

    def get_newest_item(self):
        if not self.inventory:
            return None

        newest_item = self.inventory[0]
        for item in self.inventory:
            if item.age < newest_item.age:
                newest_item = item
        return newest_item
