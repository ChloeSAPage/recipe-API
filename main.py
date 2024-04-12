import requests
from db_utils import get_recipes


def request_get_recipes():
    result = requests.get(
        'http://127.0.0.1:5001/get-recipes',
        headers={'content-type': 'application/json'}
    )
    return result.json()

def run():
    get_recipes()











if __name__ == '__main__':
    run()