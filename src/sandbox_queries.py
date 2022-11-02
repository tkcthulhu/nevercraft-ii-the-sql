from database.connections import *

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
        print(record[1])

    return record[1]

testing_print_heroes()