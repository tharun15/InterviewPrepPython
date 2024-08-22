class Pizza:
    def __init__(self):
        self.base = None
        self.patty = None
        self.cheese = None

    def set_base(self, base):
        self.base = base

    def set_patty(self, patty):
        self.patty = patty

    def set_cheese(self, cheese):
        self.cheese = cheese

    def calculate_price(self):
        base_price = self.base.get_price() if self.base else 0
        patty_price = self.patty.get_price() if self.patty else 0
        cheese_price = self.cheese.get_price() if self.cheese else 0
        return base_price + patty_price + cheese_price

    def __str__(self):
        return f"Pizza with {self.base} base, {self.patty} patty, and {self.cheese} cheese. Total price: ${self.calculate_price()}"
class Base:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return self.name

class Patty:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return self.name

class Cheese:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return self.name

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_base(self, base):
        self.pizza.set_base(base)
        return self

    def set_patty(self, patty):
        self.pizza.set_patty(patty)
        return self

    def set_cheese(self, cheese):
        self.pizza.set_cheese(cheese)
        return self

    def build(self):
        return self.pizza

# Create components
thin_crust = Base("Thin Crust", 5)
thick_crust = Base("Thick Crust", 7)
beef_patty = Patty("Beef Patty", 4)
chicken_patty = Patty("Chicken Patty", 3)
mozzarella = Cheese("Mozzarella", 2)
cheddar = Cheese("Cheddar", 3)

# Build pizza
builder = PizzaBuilder()
pizza = (builder
         .set_base(thin_crust)
         .set_patty(beef_patty)
         .set_cheese(mozzarella)
         .build())

print(pizza)
