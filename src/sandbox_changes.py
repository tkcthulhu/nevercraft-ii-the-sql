from database.connections import *

def add_new_hero():

    name = input('What hero would you like to add? ')
    about = input('Tell me about them! ')
    bio = input('What happened to make them a super hero? ')

    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
            """

    execute_query(query, (name, about, bio))

add_new_hero()

def delete_hero():

    name = input('Who did Homelander kill this time? ')

    query = """
        DELETE FROM heroes WHERE name=%s
            """

    execute_query(query, (name,))

delete_hero()