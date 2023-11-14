from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dishNum1 = Dish("sanduiche", 20)
    dishNum2 = Dish("cachorro-quente", 25)
    dishNum3 = Dish("sanduiche", 20)

    assert dishNum1.name == "sanduiche"
    assert dishNum1 == dishNum3
    assert dishNum1 != dishNum2
    assert hash(dishNum1) == hash(dishNum3)
    assert hash(dishNum2) != hash(dishNum1)
    assert repr(dishNum1) == "Dish('sanduiche', R$20.00)"
    dishNum1.add_ingredient_dependency(Ingredient("salmão"), 7)
    assert len(dishNum1.get_ingredients()) == 1
    assert dishNum1.get_restrictions()

    with pytest.raises(ValueError):
        Dish("frago-xadrez", -24)

    with pytest.raises(TypeError):
        Dish("frago-xadrez", "Tipagem errada")
