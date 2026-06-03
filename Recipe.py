class Recipe:
    def __init__(self, title, ingredients):
        self._title = title
        self._ingredients = ingredients

    def add_ingredient(self, ingredient: Ingredient):
        for ing in self._ingredients:
            if ing == ingredient:
                ing.quantity += ingredient.quantity
                return

        self._ingredients.append(ingredient)


    @property
    def title(self):
        return self._title

    @property
    def ingredients(self):
        return self._ingredients

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0

    def scale(self, ratio: float):
        new_ingredients = self._ingredients.copy()
        for ing in new_ingredients:
            ing.quantity = ing.quantity * ratio

        return Recipe(self._title, new_ingredients)

    def __len__(self):
        return len(self._ingredients)

    def __str__(self):
        text = [self._title + ":"]
        for ing in self._ingredients:
            text.append("- " + str(ing))

        return "\n".join(text)
