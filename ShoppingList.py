class ShoppingList:
    def __init__(self, items = []):
        self._items = items

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")

        scaled_recipe = recipe.scale(portions)
        for ing in scaled_recipe.ingredients:
            self._items.append((ing, scaled_recipe.title))

    def remove_recipe(self, title: str):
        self._items = [x for x in self._items if x[1] != title]

    def get_list(self):
        d = {}

        for title, ing in self._items:
            key = (ing.name, ing.unit)
            if key in d:
                d[key] += ing.quantity
            else:
                d[key] = ing.quantity

        result = [Ingredient(name, quant, unit) for (name, unit), quant in d]
        result.sort(lambda key : key.name)

        return result

    def __add__(self, other):
        return ShoppingList(self._items + other._items)
