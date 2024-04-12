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

        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result






if __name__ == '__main__':
    print("Don't run this file.")