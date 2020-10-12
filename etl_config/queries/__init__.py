import os
import psycopg2

__all__ = ['landing']

query_connection_parameters = {
    "dbname": os.environ["pg_db"],
    "user": os.environ["pg_user"],
    "password": os.environ["pg_password"],
    "host": os.environ["pg_host"],
    "port": os.environ["pg_port"]
}

query_connection_string = str(query_connection_parameters)\
    .replace(':','=')\
    .replace(' ','')\
    .replace(',',' ')\
    .replace('{','')\
    .replace('}','')\
    .replace('\'','')

def insert_data(insert_query):
    pg_connection = psycopg2.connect(query_connection_string)
    pg_handler = pg_connection.cursor()
    pg_handler.execute(insert_query)
    pg_connection.commit()
    pg_connection.close()
