from database.connections import *
from pprint import pprint as pp

def testing_function():

    execute_query("""
                    SELECT * FROM heroes
                    """)
    return 'successful'

def testing_print_heroes_info():

    print('What would you like to know about our heroes? names, about them, biographies')

    i = input().lower()

    if i == 'name':
        i = 1
    elif i == 'about me':
        i = 2
    elif i == 'biography':
        i == 3
    else:
        print('INVALID')
        return

    query = """
        SELECT * FROM heroes
        """
    
    list_of_heroes = execute_query(query).fetchall()
    
    for record in list_of_heroes:
        pp(record[int(i)])

testing_print_heroes_info()

