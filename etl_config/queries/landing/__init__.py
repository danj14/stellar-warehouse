import os

def load_sql(sql_file):
    with open(sql_file) as f:
        file_buffer = f.read()
    return file_buffer

lnd_d_product = f'{os.path.dirname(__file__)}/load_product.sql'.replace('\\','/')
