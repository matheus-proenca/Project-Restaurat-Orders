from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredientNum1 = Ingredient("salmão")
    ingredientNum2 = Ingredient("bacon")
    ingredientNum3 = Ingredient("salmão")

    assert ingredientNum1.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
    assert ingredientNum1.name == "salmão"
    assert ingredientNum1 != ingredientNum2
    assert ingredientNum1 == ingredientNum3
    assert hash(ingredientNum1) == hash(ingredientNum3)
    assert hash(ingredientNum2) != hash(ingredientNum1)
    assert Ingredient.__repr__(ingredientNum1) == "Ingredient('salmão')"
