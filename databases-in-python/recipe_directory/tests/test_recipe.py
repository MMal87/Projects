from lib.recipe import Recipe

"""Recipe constructs with id, recipe_name, cooking_time and rating """
def test_variables():
    recipe = Recipe(1, "Test Recipe", 1, 1)
    assert recipe.id == 1
    assert recipe.recipe_name == "Test Recipe"
    assert recipe.cooking_time == 1
    assert recipe.rating == 1


def test_recipes_are_equal():
    recipe_1 = Recipe(1, "Test Recipe", 1, 1)
    recipe_2 = Recipe(1, "Test Recipe", 1, 1)
    assert recipe_1 == recipe_2

"""Testing formatting"""

def test_recipes_format_nicely():
    recipe = Recipe(1, "Test Recipe", 1, 1)
    assert str(recipe) == "Recipe(1, Test Recipe, 1, 1)"
