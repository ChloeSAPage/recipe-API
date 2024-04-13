import requests
import json


def request_get_recipes():
    '''Request the titles of all the recipes'''
    result = requests.get(
        'http://127.0.0.1:5001/get-recipes',
        headers={'content-type': 'application/json'}
    )
    return result.json()


def request_get_recipe(name):
    '''Request single recipe by recipe name'''
    result = requests.get(
        'http://127.0.0.1:5001/get-recipe/{}'.format(name),
        headers={'content-type': 'application/json'}
    )
    return result.json()


def request_put_recipe(recipe):
    result = requests.put(
        'http://127.0.0.1:5001/submit-recipe',
        headers={'content-type': 'application/json'},
        data=json.dumps(recipe)
    )
    try:
        return result.json()
    except:
        return result.content


def format_response(result):
    '''
    Take result from get_recipe() and print it nicely
    '''
    print(f"\n-------------------\n {result[0][0]} \n-------------------")
    print("Ingredients:")
    for ingredient in result:
        print(f"{ingredient[2]}, {str(ingredient[3])} {ingredient[4]}")
    print(f"\n{result[0][1]}\n")


def input_recipe():
    '''Allow user to input their own recipe from the command line'''
    recipe = []

    recipe_name = input("Enter your recipe name: ")
    recipe.append(recipe_name)

    instructions = input("Enter your recipe instructions (use a \"\\n\" after each instruction): ")
    recipe.append(instructions)

    done = True
    while done:
        ingredients = []
        ingredient = input("Enter your recipe ingredient (enter 'None' when no more ingredients): ").lower()
        if ingredient == "none":
            break
        measurement = input("Enter your ingredient measurement: ")
        unit = input("Enter your ingredient unit: ")
        ingredients.append(ingredient)
        ingredients.append(measurement)
        ingredients.append(unit)
        recipe.append(ingredients)

    return recipe


def run():
    try:
        user_choice = int(input("Please select an option. \n1 - List all recipe names\n2 - Get recipe by name\n3 - Input a recipe\nEnter a number: "))
    except ValueError:
        print("Please enter a number")

    if user_choice == 1:
        # Get all recipe names in cookbook
        result = request_get_recipes()
        print(result)

    elif user_choice == 2:
        # Get whole recipe by recipe name given by user
        # Example Beans On Toast
        result = input("Enter the name of the recipe you wish to see: ")
        recipe = request_get_recipe(result)
        format_response(recipe)

    elif user_choice == 3:
        # Input Recipe
        recipe = input_recipe()
        print(request_put_recipe(recipe))
        # Print recipe that was just put in
        recipe_return = request_get_recipe(recipe[0])
        format_response(recipe_return)


if __name__ == '__main__':
    run()