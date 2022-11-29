class BusStop():
    def __init__(self,input_name):
        self.name = input_name
        self.queue = []

    def add_to_queue(self, person_object):
        self.queue.append(person_object)

    def queue_length(self):
        return len(self.queue)

    def clear(self):
        self.queue.clear()

    def pick_up_passengers(self):
        return self.queue