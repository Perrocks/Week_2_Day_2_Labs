from classes.customer import Customer

class PetShop:
    def __init__(self, shop_name, pets_list, starting_cash):
        self.name = shop_name
        self.pets_list = pets_list
        self.total_cash = starting_cash
        self.pets_sold = 0

    #methods
    def stock_count(self):
        return len(self.pets_list)
    
    def increase_pets_sold(self):
        self.pets_sold += 1

    def increase_total_cash(self, amount):
        self.total_cash += amount
    
    def remove_pet(self, pet_object):
        for pet in self.pets_list:
            if pet == pet_object:
                self.pets_list.remove(pet_object)

    def find_pet_by_name(self, pet_name):
        for pet in self.pets_list:
            if pet.name == pet_name:
                return pet

    def sell_pet_to_customer(self, pet_name, customer_object):
        pet_being_sold = self.find_pet_by_name(pet_name)
        pet_cost = pet_being_sold.price
        #reduce customer cash
        customer_object.reduce_cash(pet_cost)
        #add pet to customer
        customer_object.add_pet(customer_object)
        #add cash to shop
        self.increase_total_cash(pet_cost)
        #remove pet from shop
        self.remove_pet(pet_being_sold)
        #increase pets sold count
        self.increase_pets_sold()
