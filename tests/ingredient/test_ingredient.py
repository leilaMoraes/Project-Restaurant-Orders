from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("farinha")
    assert ingredient.name == "farinha"
    assert ingredient.restrictions == {Restriction.GLUTEN}
    assert repr(ingredient) == "Ingredient('farinha')"

    ingredient1 = Ingredient("salmão")
    ingredient2 = Ingredient("salmão")
    ingredient3 = Ingredient("presunto")
    
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)
