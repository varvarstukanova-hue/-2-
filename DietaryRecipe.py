class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients = []):
        super().__init__(title, ingredients)

        self._diet_type = diet_type

    def scale(self, ratio: float):
        return DietaryRecipe(self._title, self._diet_type, super().scale(ratio)._ingredients)

    def __str__(self):
        return "[{}] ".format(self._diet_type) + super().__str__()

