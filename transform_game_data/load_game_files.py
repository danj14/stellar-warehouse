import psycopg2
import os

pg_connection = psycopg2.connect(
    dbname=os.environ['pg_db'],
    user=os.environ['pg_user'],
    password=os.environ['pg_password'],
    host=os.environ['pg_host'],
    port=os.environ['pg_port']
)
pg_handler = pg_connection.cursor()
pg_handler.execute(
    "SELECT * FROM landing_product;"
)
pg_results = pg_handler.fetchone()
print(pg_results)
