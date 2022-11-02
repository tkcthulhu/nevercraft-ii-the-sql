from database.connections import *
from pprint import pprint as pp

def testing_function():

    execute_query("""
                    SELECT * FROM heroes
                    """)
    return 'successful'

def testing_print_heroes():

    query = """
        SELECT * FROM heroes
        """
    
    list_of_heroes = execute_query(query).fetchall()
    
    for record in list_of_heroes:
        pp(record)

testing_print_heroes()