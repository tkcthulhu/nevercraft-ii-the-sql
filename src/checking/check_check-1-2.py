from nevercraft_ii_the_sql.src.database.connections import *

def testing_print_heroes2():

    query = """
        SELECT * FROM heroes
        """
    
    list_of_heroes = execute_query(query).fetchall()
    
    for record in list_of_heroes:
        print(record[1])

    return record[1]

testing_print_heroes2()