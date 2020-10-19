import etl_config as conf
import json
import etl_config.queries.landing as landing
import etl_config.queries as exec_sql
import pgpy_lite as pg

def load_file(landing_index, landing_data):
    conf.prepare_configuration(__file__)
    load_source = conf.db_load_source
    load_queue = conf.db_load_queue

    with open(f'{load_source}/{load_queue[landing_index]}') as file_data:
        json_data = json.loads(file_data.read())
    query = landing.load_sql(landing_data[0])
    pg.query_parameter_list = pg.query_parameters(query)

    for record in json_data[landing_data[1]]:
        pg.cast_parameters(drop_missing=True, record=record)
        sql = pg.generate_query(query=query, record=record)
        exec_sql.insert_data(sql)

landing_tables = (
    (0, landing.lnd_d_product, 'lnd_d_product'),
    (1, landing.lnd_d_product_ingredient, 'lnd_d_product_ingredient'),
    (2, landing.lnd_d_substance, 'lnd_d_substance')
)

# load_file(landing_tables[0][0], landing_tables[0][1:])
load_file(landing_tables[1][0], landing_tables[1][1:])
# load_file(landing_tables[2][0], landing_tables[2][1:])

#pg.query_parameters = pg.query_parameters(query)
#pg.cast_parameters(drop_missing=True, record=json_data["lnd_d_substance"][0])
#sql = pg.generate_query(query=query, record=json_data["lnd_d_substance"][0])
#print(sql)
