import etl_config as conf
import json
import etl_config.queries.landing as landing
import etl_config.queries as exec_sql
import pgpy_lite as pg
import threading
import datetime

def load_data(query, record):
    pg.cast_parameters(drop_missing=True, record=record)
    sql = pg.generate_query(query=query, record=record)
    exec_sql.insert_data(sql)

def write_to_csv(row, file, mode):
    with open(file, mode=mode) as csv_file:
        csv_file.write(row)

def load_file(landing_data, landing_table, load_method):
    conf.prepare_configuration(__file__)
    with open(landing_data["data_file"]) as file_data:
        json_data = json.loads(file_data.read())
    query = landing.load_sql(landing_data["query_file"])
    pg.query_parameter_list = pg.query_parameters(query)

    if load_method == 'insert':
        for record in json_data[landing_data["json_object"]]:
            if 'sub_item_ref' in landing_data:
                for sub_item in record[landing_data["sub_item_ref"]]:
                    sub_item["parent_id"] = record[landing_data["sub_item_parent_alias"]]
                    load_data(query=query, record=sub_item)
            else:
                load_data(query=query, record=record)
    elif load_method == 'copy':
        # TODO: need to cast data
        # TODO: fix .csv (cast data too and change column names to match table)
        # TODO: fix order of "parent_id" column (needs to be first)
        # TODO: write csv file to SFTP folder (a few options; one way is to follow this article: https://gist.github.com/bortzmeyer/1284249"
        #       ...else, we could use Paramiko
        # TODO: execute final "copy" command
        headers = []
        item_list = []
        for record in json_data[landing_data["json_object"]]:
            if 'sub_item_ref' in landing_data:
                item_list_row = []

                for sub_item in record[landing_data["sub_item_ref"]]:
                    sub_item["parent_id"] = record[landing_data["sub_item_parent_alias"]]
                    for k,v in sub_item.items():
                        if len(headers) < len(sub_item.keys()) and k not in headers:
                            headers.append(k)
                        item_list_row.append(v)
                    item_list.append(item_list_row)
            else:
                pass
        write_to_csv(','.join(headers)+'\n', f'{conf.db_copy_source}/{landing_data["json_object"]}.csv', 'w')
        for item in item_list:
            write_to_csv(','.join(item)+'\n', f'{conf.db_copy_source}/{landing_data["json_object"]}.csv', 'a')
    else:
        print(f'ERROR: Load method value "{load_method}" is not a valid call...exiting process')
        exit(-1)

landing_tables = {
    "lnd_d_product": {
        "data_file": f'{conf.db_load_source}/lnd_d_product.json',
        "json_object": 'lnd_d_product',
        "query_file": landing.lnd_d_product
    },
    "lnd_d_product_ingredient": {
        "data_file": f'{conf.db_load_source}/lnd_d_product.json',
        "json_object": 'lnd_d_product',
        "query_file": landing.lnd_d_product_ingredient,
        "sub_item_ref": 'Requirements',
        "sub_item_parent_alias": 'Id'
    },
    "lnd_d_substance": {
        "data_file": f'{conf.db_load_source}/lnd_d_substance.json',
        "json_object": 'lnd_d_substance',
        "query_file": landing.lnd_d_substance
    }
}

# multi_trial_start = datetime.datetime.now()
# thread1 = threading.Thread(target=load_file(landing_tables["lnd_d_product"], 'lnd_d_product'))
# thread2 = threading.Thread(target=load_file(landing_tables["lnd_d_product_ingredient"], 'lnd_d_product_ingredient'))
# thread3 = threading.Thread(target=load_file(landing_tables["lnd_d_substance"], 'lnd_d_substance'))
# thread1.start()
# thread2.start()
# thread3.start()
# multi_trial_end = datetime.datetime.now()

# single_trial_start = datetime.datetime.now()
# [x] load_file(landing_tables["lnd_d_product"], 'lnd_d_product', 'copy')
# TODO: think about writing JSON data to .CSV and using COPY instead of row-by-row inserts
load_file(landing_tables["lnd_d_product_ingredient"], 'lnd_d_product_ingredient', 'copy')
# load_file(landing_tables["lnd_d_substance"], 'lnd_d_substance')
# single_trial_end = datetime.datetime.now()

# print(f'm: {multi_trial_start} || s: {single_trial_start}')
# print(f'm: {multi_trial_end} || s: {single_trial_end}')
