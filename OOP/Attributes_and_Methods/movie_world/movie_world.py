class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        output = ''
        for c in self.customers:
            output += c.__repr__() + '\n'
        for d in self.dvds:
            output += d.__repr__() + '\n'
        return output.rstrip()

    def add_customer(self, customer):
        capacity = MovieWorld.customer_capacity()
        if len(self.customers) < capacity:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        capacity = MovieWorld.dvd_capacity()
        if len(self.dvds) < capacity:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer_found = [c for c in self.customers if c.id == customer_id]
        customer_obj = customer_found[0]
        dvd_found = [d for d in self.dvds if d.id == dvd_id]
        dvd_obj = dvd_found[0]
        if dvd_obj.is_rented and dvd_obj in customer_obj.rented_dvds:
            return f"{customer_obj.name} has already rented {dvd_obj.name}"
        if dvd_obj.is_rented:
            return "DVD is already rented"
        if customer_obj.age < dvd_obj.age_restriction:
            return f"{customer_obj.name} should be at least {dvd_obj.age_restriction} " \
                   f"to rent this movie"
        dvd_obj.is_rented = True
        customer_obj.rented_dvds.append(dvd_obj)
        return f"{customer_obj.name} has successfully rented {dvd_obj.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer_found = [c for c in self.customers if c.id == customer_id]
        customer_obj = customer_found[0]
        dvd_found = [d for d in self.dvds if d.id == dvd_id]
        dvd_obj = dvd_found[0]
        if dvd_obj in customer_obj.rented_dvds:
            customer_obj.rented_dvds.remove(dvd_obj)
            dvd_obj.is_rented = False
            return f"{customer_obj.name} has successfully returned {dvd_obj.name}"
        return f"{customer_obj.name} does not have that DVD"

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10