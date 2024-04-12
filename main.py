import requests
from db_utils import get_recipes, get_recipe


def request_get_recipes():
    result = requests.get(
        'http://127.0.0.1:5001/get-recipes',
        headers={'content-type': 'application/json'}
    )
    return result.json()


def request_get_recipe(name):
    result = requests.get(
        'http://127.0.0.1:5001/get-recipe/{}'.format(name),
        headers={'content-type': 'application/json'}
    )
    return result.json()

def input_recipe():
    recipe = []

    recipe_name = input("Enter your recipe name: ")
    recipe.append(recipe_name)

    instructions = input("Enter your recipe instructions (use a \"\\n\" after each instruction then hit enter): ")
    recipe.append(instructions)

    done = True
    while done:
        ingredients = []
        ingredient = input("Enter your recipe ingredient (enter 'None' when no more ingredients): ")
        if ingredient == "None":
            break
        measurement = input("Enter your ingredient measurement: ")
        unit = input("Enter your ingredient unit: ")
        ingredients.append(ingredient)
        ingredients.append(measurement)
        ingredients.append(unit)
        recipe.append(ingredients)

    print(recipe)
    return recipe


def format_response(result):
    print(result[0][0])
    print("Ingredients:")
    for ingredient in result:
        print(f"{ingredient[2]}, {str(ingredient[3])} {ingredient[4]}")
    print(result[0][1])



def run():
    # result = request_get_recipes()
    # print(result)
    # result = request_get_recipe('Beans On Toast')
    # format_response(result)
    input_recipe()











if __name__ == '__main__':
    run()