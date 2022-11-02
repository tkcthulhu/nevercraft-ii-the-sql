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

# testing_print_heroes_info()

def get_hero_by_name():
    i = input('Which hero would you like to know about? ')

    i = str(i)

    find_hero = """
            SELECT * FROM heroes
            WHERE name=%s
                """

    print(find_hero)

    hero = execute_query(find_hero, (i,))

    for info in hero:
        pp(info)

    

get_hero_by_name()