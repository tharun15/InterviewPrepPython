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
        if self.base:
            base_price = self.base.get_price()
        else:
            base_price = 0

        if self.patty:
            patty_price = self.patty.get_price()
        else:
            patty_price = 0

        if self.cheese:
            cheese_price = self.cheese.get_price()
        else:
            cheese_price = 0
        return base_price + patty_price + cheese_price
    
    def __str__(self):
        return f'{self.calculate_price()}'


class Base:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price
    
class Patty:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class Cheese:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price
#Pizza = new PizzaBuilder.base(new thinCrust()).sauce(new Marinara()).cheese(new Mozzarella()).build();
# Sysout pizza.getPrice();    
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_base(self, base):
        self.pizza.base = base
        return self

    def set_patty(self, patty):
        self.pizza.patty = patty
        return self
    
    def set_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self
    
    def build(self):
        return self.pizza
    

thin_crust = Base("Thin Crust", 5)
thick_crust = Base("Thin Crust", 7)
veg_patty = Patty("Veg Patty", 3)
chicken_patty = Patty("Chicken Patty", 3)
mozzarella = Cheese("Mozzarella", 2)
cheddar = Cheese("Cheddar", 3)

builder = PizzaBuilder()

pizza = builder.set_base(thin_crust).set_patty(veg_patty).set_cheese(cheddar).build()

print(pizza)