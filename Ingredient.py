class Ingredient:
    def __init__(self, name, quantity, unit):
        self._name = name
        self._quantity = quantity
        self._unit = unit

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")

        self._quantity = float(value)

    def __str__(self):
        return "{}: {} {}".format(self._name, self._quantity, self._unit)

    def __repr__(self):
        return "Ingredient('{}', {}, '{}')".format(self._name, self._quantity, self._unit)

    def __eq__(self, other):
        return self._name == other._name and self._unit == other._unit
