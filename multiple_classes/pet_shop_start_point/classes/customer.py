from classes.pet import Pet

class Customer():
    def __init__(self, input_name, input_cash):
        self.name = input_name
        self.cash = input_cash
        self.pets = [ ]
    
    #Methods
    def add_pet(self, pet_object):
        self.pets.append(pet_object)

    def reduce_cash(self, amount):
        self.cash -= amount

    def pet_count(self):
        return len(self.pets)

    def get_total_value_of_pets(self):
        total = 0
        for pet in self.pets:
            total += pet.price
        return total