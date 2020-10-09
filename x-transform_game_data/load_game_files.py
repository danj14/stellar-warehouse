import psycopg2
import os
from transform_game_data import pg_py_lite

class GameFileLoader:
    def __init__(self):
        self.connection_config = f'dbname={os.environ["pg_db"]} ' \
                                 f'user={os.environ["pg_user"]} ' \
                                 f'password={os.environ["pg_password"]} ' \
                                 f'host={os.environ["pg_host"]} ' \
                                 f'port={os.environ["pg_port"]}'

    def execute_load(self, data, query):
        pg_connection = psycopg2.connect(self.connection_config)
        pg_handler = pg_connection.cursor()

        py_query = pg_py_lite.PgPyLite(data, query)
        py_query.convert_parameters(drop_missing=True)
        executable_query = py_query.executable_query()

        pg_handler.execute(executable_query)
        pg_connection.commit()
        pg_connection.close()
