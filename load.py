import etl_config as conf
import json
import etl_config.queries.landing as landing
import etl_config.queries as exec_sql
import pgpy_lite as pg
# from conf import queries
# import json

conf.prepare_configuration(__file__)

# TODO: replace w/loop of JSON files
load_source = conf.db_load_source
load_queue = conf.db_load_queue
with open(f'{load_source}/{load_queue[0]}') as file_data:
    json_data = json.loads(file_data.read())

query = landing.load_sql(landing.lnd_d_product)
pg.query_parameters = pg.query_parameters(query)
for record in json_data["lnd_d_product"]:
    pg.cast_parameters(drop_missing=True, record=record)
    sql = pg.generate_query(query=query, record=record)
    exec_sql.insert_data(sql)

"""
def load_game_files(temp_debug_json):
    # switch to loading a file instead of in-memory
    query_config_file = open('transform_game_data/landing_tables_load_config.json')
    query_config = query_config_file.read()
    query_config_file.close()
    query_config = json.loads(query_config)
    query_file = open(query_config['product'], 'r')
    query = query_file.read()
    query_file.close()
    
    data_loader = loader.GameFileLoader()
    for record in temp_debug_json['lnd_d_product']:
        data_loader.execute_load(data=record, query=query)
"""