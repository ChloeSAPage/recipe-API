import mysql.connector
from config import HOST, USER, PASSWORD

class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def get_recipes():
    ''' Get all the recipe names from the cookbook db'''
    try:
        db_name = 'cookbook'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            SELECT title
            FROM recipes
            """

        cur.execute(query)

        result = cur.fetchall()  # this is a list of all recipe names, where each recipe name is a list.
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result

def get_recipe(name):
    '''Get a single recipe name from the cookbook db based on the users input'''
    try:
        db_name = 'cookbook'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            SELECT r.title, r.instructions, i.ingredient, i.measurement, i.unit
            FROM recipes r
            INNER JOIN ingredients i
            ON r.recipe_id = i.recipe_id
            WHERE r.title = "{}";
            """.format(name)

        cur.execute(query)

        result = cur.fetchall()  # this is a list of all recipe names, where each recipe name is a list.
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result


def insert_recipe(recipe):
    '''Insert the user given recipe into cookbook db'''
    try:
        db_name = 'cookbook'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        # insert recipe name into recipes table
        # recipe = ['Microwave Bacon', '1. Microwave Bacon \\n 2. Eat', ['Bacon', '2', 'rashers'], ['Bread', '2', 'Slices']]
        title = recipe[0]
        instructions = recipe[1]
        query = """
            INSERT INTO recipes
            (title, instructions)
            VALUES
            ("{title}", "{instructions}")
            """.format(title=title, instructions=instructions)

        cur.execute(query)
        db_connection.commit()

        # get recipe ID from recipe table in order to place the ingredients in table
        # cur.execute(query)
        # result = cur.fetchall()

        # for loop inserting ingredient into ingredient table
        # cur.execute(query)
        # result = cur.fetchall()

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")






if __name__ == '__main__':
    print("Don't run this file.")