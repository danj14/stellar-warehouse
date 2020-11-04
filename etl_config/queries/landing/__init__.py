import os

def load_sql(sql_file):
    with open(sql_file) as f:
        file_buffer = f.read()
    return file_buffer

lnd_d_product = f'{os.path.dirname(__file__)}/load_product.sql'.replace('\\','/')
lnd_d_product_ingredient = f'{os.path.dirname(__file__)}/load_product_ingredient.sql'.replace('\\','/')
lnd_d_substance = f'{os.path.dirname(__file__)}/load_substance.sql'.replace('\\','/')
landing_copy = f'{os.path.dirname(__file__)}/load_by_copy.sql'.replace('\\', '/')
