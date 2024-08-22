class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def print(self):
        print(self.ingredients)


class BurgerFactory:

    def createCheeseBurger(self):
        ingredients = ["bun", "cheese","patty"]

        return Burger(ingredients)
    
    def createVeggieBurger(self):
        ingredients = ["bun", "cheese", "vegetables"]

        return Burger(ingredients)
    

burgerFactory = BurgerFactory()
burgerFactory.createVeggieBurger().print()