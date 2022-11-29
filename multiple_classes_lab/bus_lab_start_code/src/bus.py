class Bus():
    def __init__(self, bus_no, bus_dest):
        self.route_number = bus_no
        self.destination = bus_dest
        self.number_of_passengers = 0
        self.passenger_list = []

    #Methods
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return self.number_of_passengers

    def pick_up(self, person_object):
        self.passenger_list.append(person_object)
        self.number_of_passengers += 1
    
    def drop_off(self, person_object):
        self.passenger_list.remove(person_object)
        self.number_of_passengers -= 1

    def empty(self):
        self.passenger_list.clear()
        self.number_of_passengers = 0

    def pick_up_from_stop(self, bus_stop_object):
        people_picked_up = bus_stop_object.pick_up_passengers()
        for person in people_picked_up:
            self.pick_up(person)
        bus_stop_object.clear()
        
        