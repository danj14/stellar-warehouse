import etl_config as conf
import json
import etl_config.queries.landing as landing
import etl_config.queries as exec_sql
import pgpy_lite as pg
import threading
import datetime

def load_data(query, record, drop_missing, query_type):
    pg.cast_parameters(drop_missing=drop_missing, record=record)
    sql = pg.generate_query(query=query, record=record, query_type=query_type)
    print (sql)
    # TODO: rename method to something more generic exec_sql.insert_data(sql)

def write_to_csv(row, file, mode):
    with open(file, mode=mode) as csv_file:
        csv_file.write(row)

def cast_data(query):
    pg.query_parameter_list = pg.query_parameters(query)

def localize_data(origin, destination):
    pass

def load_file(landing_data, load_method):
    conf.prepare_configuration(__file__)
    with open(landing_data["data_file"]) as file_data:
        json_data = json.loads(file_data.read())

    if load_method == 'insert':
        query = landing.load_sql(landing_data["query_file"])
        cast_data(query)
        for record in json_data[landing_data["json_object"]]:
            if 'sub_item_ref' in landing_data:
                for sub_item in record[landing_data["sub_item_ref"]]:
                    sub_item["parent_id"] = record[landing_data["sub_item_parent_alias"]]
                    load_data(query=query, record=sub_item, drop_missing=True, query_type=load_method)
            else:
                load_data(query=query, record=record, drop_missing=True, query_type=load_method)
    elif load_method == 'copy':
        query = landing.load_sql(landing.landing_copy)
        cast_data(query)
        # [3] TODO: need to cast data
        # [X] TODO: fix .csv (cast data too and change column names to match table)
        # [2] TODO: fix order of "parent_id" column (needs to be first)
        # [1] TODO: write csv file to SFTP folder (a few options; one way is to follow this article: https://gist.github.com/bortzmeyer/1284249"
        #       ...else, we could use Paramiko [try to avoid]
        #       ...Try following the idea of using a subprocess (https://docs.python.org/3/library/subprocess.html)
        #       ...==> But remember we are running this initial prototype off Windows (need to address this in some way
        #       ...==::once we need to handle environment promotion)
        #       ...==> I'm thinking we execute Putty from a powershell file (need to lookup how to do that); should be ez
        # [4] TODO: execute final "copy" command
        headers = []
        item_rows = []
        csv_file_path = f'{conf.db_copy_source}/{landing_data["csv_table_name"]}.csv'
        for record in json_data[landing_data["json_object"]]:
            if 'sub_item_ref' in landing_data:
                item_ingredient_rows = []
                for sub_item in record[landing_data["sub_item_ref"]]:
                    sub_item["parent_id"] = record[landing_data["sub_item_parent_alias"]]
                    item_ingredient_row = []
                    for k,v in sub_item.items():
                        if len(headers) < len(sub_item.keys()) and k not in headers:
                            table_header = k
                            headers.append(table_header)
                        item_ingredient_row.append(v)
                    item_ingredient_rows.append(item_ingredient_row)
                item_rows.append({"item_ingredient_rows": item_ingredient_rows})
            else:
                pass
        #write_to_csv(','.join(headers)+'\n', csv_file_path, 'w')
        #for item in item_rows:
            #if 'item_ingredient_rows' in item:
                #item_ingredient_rows = [sub_items for sub_items in item['item_ingredient_rows']]
                #for item_ingredient in item_ingredient_rows:
                #    write_to_csv(','.join(item_ingredient)+'\n',
                #                 csv_file_path, 'a')
            #else:
                #pass
        # TODO: localized_data = localize_data(origin=csv_file_path, destination=conf.)
        load_data(query=query,
                  record={
                      "landing_csv": csv_file_path,
                      "landing_table": landing_data["csv_table_name"]
                  }, drop_missing=False, query_type=load_method)
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
        "csv_table_name": "lnd_d_product_ingredient",
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
load_file(landing_tables["lnd_d_product_ingredient"], 'copy')
# load_file(landing_tables["lnd_d_substance"], 'lnd_d_substance')
# single_trial_end = datetime.datetime.now()

# print(f'm: {multi_trial_start} || s: {single_trial_start}')
# print(f'm: {multi_trial_end} || s: {single_trial_end}')
