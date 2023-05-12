from lib.recipe import Recipe
from lib.recipe_repository import RecipeRepository

"""When all function is called, the class will display a list of all recipes"""
def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipes = repository.all()
    assert recipes == [
        Recipe(1, 'Daal', 90, 1),
        Recipe(2, 'Mexican Bean Stew', 180, 3),
        Recipe(3, 'Carrot Cake', 180, 2),
        Recipe(4, 'Chicken Milanese', 60, 2),
        Recipe(5, 'Leek and Potato Soup', 180, 2),
        Recipe(6, 'Creme Brulee', 55, 5)
    ]

"""When find method is called using id, return the value linked to that id"""

def test_find(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find(2)
    assert recipe == Recipe(2, 'Mexican Bean Stew', 180, 3)

