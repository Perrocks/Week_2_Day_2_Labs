from classes.customer import Customer

class PetShop:
    def __init__(self, input_shop_name, input_pets_list, input_starting_cash):
        self.name = input_shop_name
        self.pets_list = input_pets_list
        self.total_cash = input_starting_cash
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

    #Alt method for remove_pet
    def remove_pet(self, pet_object): 
        self.pets_list.remove(pet_object)

    def find_pet_by_name(self, pet_name):
        for pet in self.pets_list:
            if pet.name == pet_name:
                return pet

    def check_pet_exists(self, pet_name):
        if self.find_pet_by_name(pet_name):
            print("That pet is not in stock!")
            return True
        return False

    def sell_pet_to_customer(self, pet_name, customer_object):
        #check transaction possible
        if self.check_pet_exists(pet_name):
            #variable assignments
            pet_being_sold = self.find_pet_by_name(pet_name)
            pet_cost = pet_being_sold.price
            #functions
            customer_object.reduce_cash(pet_cost)
            customer_object.add_pet(customer_object)
            self.increase_total_cash(pet_cost)
            self.remove_pet(pet_being_sold)
            self.increase_pets_sold()



#Lists in a Program

list_of_strings  = ["Here is a string", "Here is another", "here is a third"]
list_of_ints = [0, 1, 3, 5, 7]

def my_list_using_function(list_a, list_b):
    lower_case_list = []
    for item in list_a:
        item.lower()
        lower_case_list.append(item)
    return lower_case_list

