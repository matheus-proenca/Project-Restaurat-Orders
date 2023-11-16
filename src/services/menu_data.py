import csv
from models.ingredient import Ingredient
from models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path) as file:
            data = csv.reader(file, delimiter=",")
            next(data, None)
            for dish, price, ingredient, amount in data:
                dish_ingredient = Ingredient(ingredient)
                dish_list = Dish(dish, float(price))
                if dish_list not in self.dishes:
                    dish_list.add_ingredient_dependency(
                        dish_ingredient, int(amount)
                    )
                    self.dishes.add(dish_list)
                else:
                    for item in self.dishes:
                        if item.name == dish:
                            item.add_ingredient_dependency(
                                dish_ingredient, int(amount)
                            )
