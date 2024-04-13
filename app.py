from flask import Flask
from db_utils import get_recipes, get_recipe, insert_recipe

app = Flask(__name__)


@app.route('/')
def index():
    return """This is a recipe API, you can retrieve, and submit recipes. See README for endpoints."""


@app.route('/get-recipes')
def call_get_recipes():
    result = get_recipes()
    return result



@app.route('/get-recipe/<name>')
def call_get_recipe(name):
    result = get_recipe(name)
    return result


@app.route('/submit-recipe', methods=["PUT"])
def call_insert_recipe():
    insert_recipe()
    pass



if __name__ == '__main__':
    app.run(debug=True, port=5001)
