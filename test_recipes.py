
#1 тест
import pytest
def test_ingredient_init():
    ing1 = Ingredient('Мука', 500.0, 'г')

    assert ing1._name == 'Мука'
    assert ing1._quantity == 500.0
    assert ing1._unit == 'г'


def test_ingredient_str():
    ing1 = Ingredient('Мука', 500.0, 'г')

    assert str(ing1) == "Мука: 500.0 г"


def test_ingredient_eq():
    ing1 = Ingredient('Мука', 500.0, 'г')
    ing2 = Ingredient('Мука', 100.0, 'г')
    ing3 = Ingredient('Томат', 100.0, 'г')
    ing4 = Ingredient('Мука', 100.0, 'кг')

    assert ing1 == ing2
    assert ing1 != ing3
    assert ing1 != ing4

#2 тест
def test_recipe_init():
    rec1 = Recipe(
        "Маргарита",
        [Ingredient("Мука", 500.0, 'г'), Ingredient("Томаты", 300.0, 'г')]
    )

    assert rec1._title == "Маргарита"
    assert rec1._ingredients == [Ingredient("Мука", 500.0, 'г'), Ingredient("Томаты", 300.0, 'г')]


def test_recipe_add_ingredient():
    rec1 = Recipe("Маргарита", [])
    rec1.add_ingredient(Ingredient("Мука", 500.0, 'г'))

    assert len(rec1._ingredients) == 1

    rec1.add_ingredient(Ingredient("Мука", 100.0, 'г'))

    assert len(rec1._ingredients) == 1
    assert rec1._ingredients[0].quantity == 600.0

    rec1.add_ingredient(Ingredient("Томат", 1.0, 'кг'))

    assert len(rec1._ingredients) == 2


def test_recipe_scale():
    rec1 = Recipe(
        "Маргарита",
        [Ingredient("Мука", 500.0, 'г')]
    )

    rec2 = rec1.scale(2.0)

    assert rec1._ingredients[0].quantity == 500.0
    assert rec2._ingredients[0].quantity == 1000.0

    with pytest.raises(ValueError):
        rec1.scale(-1.0)


def test_recipe_len():
    rec1 = Recipe("Маргарита", [])
    rec1.add_ingredient(Ingredient("Мука", 500.0, 'г'))
    rec1.add_ingredient(Ingredient("Мука", 100.0, 'г'))
    rec1.add_ingredient(Ingredient("Томат", 1.0, 'кг'))

    assert len(rec1._ingredients) == 2
#3 тест
def test_shop_add_recipe():
    shop = ShoppingList()

    rec1 = Recipe(
        "Маргарита",
        [Ingredient("Томаты", 300.0, 'г')]
    )
    rec2 = Recipe(
        "Цезарь",
        [Ingredient("Томаты", 300.0, 'г')]
    )

    shop.add_recipe(rec1, 1.0)
    shop.add_recipe(rec2, 2.0)

    assert shop._items == [
        (Ingredient("Томаты", 300.0, 'г'), "Маргарита"),
        (Ingredient("Томаты", 600.0, 'г'), "Цезарь")
    ]

    with pytest.raises(ValueError):
        shop.add_recipe(rec1, -1.0)


def test_shop_remove_recipe():
    shop = ShoppingList()

    rec1 = Recipe(
        "Маргарита",
        [Ingredient("Томаты", 300.0, 'г')]
    )
    rec2 = Recipe(
        "Цезарь",
        [Ingredient("Томаты", 300.0, 'г')]
    )

    shop.add_recipe(rec1, 1.0)
    shop.add_recipe(rec2, 2.0)
    shop.remove_recipe("Маргарита")

    assert all([x[1] != "Маргарита" for x in shop._items])

    shop.remove_recipe("Маргарита")


def test_shop_get_list():
    shop = ShoppingList()

    rec1 = Recipe(
        "Маргарита",
        [Ingredient("Томаты", 300.0, 'г'), Ingredient("Сыр", 300.0, 'г')]
    )
    rec2 = Recipe(
        "Цезарь",
        [Ingredient("Томаты", 300.0, 'г'), Ingredient("Сыр", 300.0, 'г')]
    )

    shop.add_recipe(rec1, 1.0)
    shop.add_recipe(rec2, 1.0)

    items = shop.get_items()
    real_items = [Ingredient("Сыр", 600.0, 'г'), Ingredient("Томаты", 600.0, 'г')]

    assert items == real_items and items[0].quantity == 600.0 and items[1].quantity == 600.0


def test_shop_add():
    shop1 = ShoppingList()
    shop2 = ShoppingList()

    rec1 = Recipe(
        "Маргарита",
        [Ingredient("Томаты", 300.0, 'г'), Ingredient("Сыр", 300.0, 'г')]
    )
    rec2 = Recipe(
        "Цезарь",
        [Ingredient("Томаты", 300.0, 'г'), Ingredient("Сыр", 300.0, 'г')]
    )

    shop1.add_recipe(rec1, 1.0)
    shop2.add_recipe(rec2, 1.0)

    shop3 = shop1 + shop2

    assert len(shop1._items) == 2
    assert len(shop2._items) == 2
    assert len(shop3._items) == 4
