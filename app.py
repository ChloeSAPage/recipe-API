from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "This is a recipe API, you can retrieve, and submit recipes"


@app.route('/recipes')
def recipes():
    return {
        "Recipes": {
            "Beans On Toast": {
                "Ingredients": ["Baked Beans", "Bread", "Butter"],
                "Instructions": {
                    1: "Cook the beans following package instructions",
                    2: "Toast the Bread",
                    3: "Butter the bread",
                    4: "Put Beans on Bread",
                    5: "Enjoy!"
                }
            },
            "Cereal": {
                "Ingredients": ["Cereal", "Milk"],
                "Instructions": {
                    1: "Get a bowl",
                    2: "Pour cereal into bowl",
                    3: "Pour Milk into bowl"
                }
            }
        }
    }



if __name__ == '__main__':
    app.run(debug=True)
