import csv
from typing import Set
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        self.ingredients = set()
        self._read_menu_data(source_path)

    def _read_menu_data(self, source_path: str) -> None:
        with open(source_path, newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                dish_name = row[0]
                price = float(row[1])
                ingredient_name = row[2]
                quantity = int(row[3])

                ingredient = Ingredient(ingredient_name)
                self.ingredients.add(ingredient)

                dish = next(
                    (d for d in self.dishes if d.name == dish_name), None)
                if dish is None:
                    dish = Dish(dish_name, price)
                    self.dishes.add(dish)

                dish.add_ingredient_dependency(ingredient, quantity)
