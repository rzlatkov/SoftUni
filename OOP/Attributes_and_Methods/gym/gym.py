class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        output = ''

        filtered_sub = [s for s in self.subscriptions if s.id == subscription_id]
        sub = filtered_sub[0]
        output += sub.__repr__() + '\n'

        filtered_cust = [c for c in self.customers if c.id == sub.customer_id]
        cust = filtered_cust[0]
        output += cust.__repr__() + '\n'

        filtered_tr = [t for t in self.trainers if t.id == sub.trainer_id]
        tr = filtered_tr[0]
        output += tr.__repr__() + '\n'

        filtered_plan = [p for p in self.plans if tr.id == p.trainer_id]
        plan = filtered_plan[0]

        filtered_eq = [e for e in self.equipment if e.id == plan.equipment_id]
        equip = filtered_eq[0]
        output += equip.__repr__() + '\n'

        output += plan.__repr__()

        return output
