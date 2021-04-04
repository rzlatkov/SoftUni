class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = quantity
        else:
            self.ingredients[ingredient] += quantity
        self.price += ingredient_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= ingredient_price * quantity

    def make_order(self):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

        self.ordered = True
        output = f"You've ordered pizza {self.name} prepared with "
        for key, value in self.ingredients.items():
            output += f"{key}: {value}, "
        output = output[:-2]
        output += f" and the price will be {self.price}lv."
        return output