import etl_config as conf
import json
import etl_config.queries.landing as landing
import etl_config.queries as exec_sql
import pgpy_lite as pg

conf.prepare_configuration(__file__)

# TODO: replace w/loop of JSON files
load_source = conf.db_load_source
load_queue = conf.db_load_queue
# with open(f'{load_source}/{load_queue[0]}') as file_data:
with open(f'{load_source}/{load_queue[0]}') as file_data:
    json_data = json.loads(file_data.read())


query = landing.load_sql(landing.lnd_d_substance)
pg.query_parameters = pg.query_parameters(query)
pg.cast_parameters(drop_missing=True, record=json_data["lnd_d_substance"][0])
sql = pg.generate_query(query=query, record=json_data["lnd_d_substance"][0])
print(sql)


# query = landing.load_sql(landing.lnd_d_product)
# pg.query_parameters = pg.query_parameters(query)
# for record in json_data["lnd_d_product"]:
#     pg.cast_parameters(drop_missing=True, record=record)
#     sql = pg.generate_query(query=query, record=record)
#     exec_sql.insert_data(sql)
