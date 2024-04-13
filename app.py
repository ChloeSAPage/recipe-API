from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "This is a recipe API, you can retrieve, and submit recipes"

@app.route('/get-recipe')
def get_recipe():
    return "This is in development"

if __name__ == '__main__':
    app.run(debug=True)
