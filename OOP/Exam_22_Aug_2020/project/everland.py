
class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for r in self.rooms:
            total_consumption += r.room_cost + r.expenses
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        to_be_removed = []
        output = ''
        for r in self.rooms:
            monthly = r.room_cost + r.expenses
            if r.budget < monthly:
                output += f"{r.family_name} does not have enough budget and must leave the hotel.\n"
                to_be_removed.append(r)
            else:
                r.budget -= monthly
                output += f"{r.family_name} paid {monthly:.2f}$ and have {r.budget:.2f}$ left.\n"

        for tobe in to_be_removed:
            self.rooms.remove(tobe)

        return output.rstrip('\n')

    def status(self):
        output = ''
        members_count = [r.members_count for r in self.rooms]
        output += f"Total population: {sum(members_count)}\n"
        for r in self.rooms:
            output += f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$\n"
            if r.children:
                for i in range(len(r.children)):
                    cost = r.children[i].get_monthly_expense()
                    output += f"--- Child {i+1} monthly cost: {cost:.2f}$\n"
            if hasattr(r, 'appliances'):
                cost_app = 0
                for i in range(len(r.appliances)):
                    cost_app += r.appliances[i].get_monthly_expense()
                output += f"--- Appliances monthly cost: {cost_app:.2f}$\n"

        return output.rstrip('\n')
