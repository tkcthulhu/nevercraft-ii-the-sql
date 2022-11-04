from database.connections import *
from pprint import pprint as pp


# CREATE

def add_new_hero():

    name = input('What hero would you like to add? ')
    about = input('Tell me about them! ')
    bio = input('What happened to make them a super hero? ')

    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
            """

    execute_query(query, (name, about, bio))

#READ

def print_heroes_info():

    i = input('What would you like to know about our heroes? names, about them, biographies ').lower()

    if i == 'names':
        i = 1
    elif i == 'about them':
        i = 2
    elif i == 'biographies':
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

def get_hero_by_name():

    i = input('Which hero would you like to know about? ')

    find_hero = """
            SELECT * FROM heroes
            WHERE name=%s
                """

    hero = execute_query(find_hero, (i,))

    for info in hero:
        pp(info)


#UPDATE

def change_hero_info():

    print('Who would you like to update? ')

    names_query = """
        SELECT name FROM heroes    
            """

    names = execute_query(names_query).fetchall()

    for name in names:
        pp(name)

    i = input()

    query1 = """
        SELECT id FROM heroes
        WHERE name = %s
            """

    id = execute_query(query1, (i,)).fetchone()

    id = id[0]

    attr = input("""
        What would you like to update?
        Name
        About me
        Biography
        """).lower()

    query2 = ''

    if attr == 'name':
        query2 = """
        UPDATE heroes
        SET name = %s
        WHERE id = %s
            """
    elif attr == 'about me':
        query2 = """
        UPDATE heroes
        SET about_me = %s
        WHERE id = %s
            """
    elif attr == 'biography':
        query2 = """
        UPDATE heroes
        SET biography = %s
        WHERE id = %s
            """

    new_attr = input("""
        What would you like to set it to?
            """)


    execute_query(query2, (new_attr, id,))
    

# DELETE

def delete_hero():

    name = input('Who did Homelander kill this time? ')

    query = """
        DELETE FROM heroes WHERE name=%s
            """

    execute_query(query, (name,))

    print('I say you they dead')

#Begin interactive program

def choose_your_path():
    i = input("""
        What would you like to do? 
        1) Create a Hero 
        2) Learn about a Hero 
        3) See all Heroes 
        4) Update Hero info
        5) Delete a Hero
        
        """)

    if i == '1': add_new_hero()
    elif i == '2': get_hero_by_name()
    elif i == '3' : print_heroes_info()
    elif i == '4': change_hero_info()
    elif i == '5': delete_hero()
    else: print('Please refer to documentation for valid commands')
    
    more()

def more() :
    i = input('Would you like to do anything else while you are here? yes no ')
    if i.lower() == 'yes': choose_your_path()
    else: return


choose_your_path()
