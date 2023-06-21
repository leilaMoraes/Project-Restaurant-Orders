from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest

# Req 2
def test_dish():
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("lasanha", 0)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("lasanha", "dez")

    dish = Dish("lasanha", 10)
    assert dish.name == "lasanha"
    assert repr(dish) == "Dish('lasanha', R$10.00)"

    dish1 = Dish("pizza", 24.50)
    dish2 = Dish("pizza", 24.50)
    dish3 = Dish("salada", 12.90)

    assert dish1 == dish2
    assert dish1 != dish3

    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)

    ingredient = Ingredient("queijo mussarela")

    dish.add_ingredient_dependency(ingredient, 1)

    assert dish.recipe == {ingredient: 1}
    assert dish.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert dish.get_ingredients() == {ingredient}
