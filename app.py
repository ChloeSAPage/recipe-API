from flask import Flask
from db_utils import get_recipes

app = Flask(__name__)


@app.route('/')
def index():
    return "This is a recipe API, you can retrieve, and submit recipes"


@app.route('/get-recipes')
def call_get_recipes():
    result = get_recipes()
    return result


# id is primary key
@app.route('/get-recipe/<id>')
def get_recipe():
    pass


@app.route('/submit-recipe', methods=["PUT"])
def submit_recipes():
    pass



if __name__ == '__main__':
    app.run(debug=True, port=5001)
