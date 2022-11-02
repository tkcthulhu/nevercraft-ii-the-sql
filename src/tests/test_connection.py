from database.connections import *

def test_initial_connection():
    assert execute_query("""
                    SELECT * FROM heroes
                    """)

                    