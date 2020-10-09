import etl_config as conf
from shutil import copy, rmtree
import os
import json
# debugging only
import extract

def prepare_files():
    # TODO: refactor to check for "finish" file once that is implemented
    if not conf.job_started:
        os.mkdir(conf.job_destination)
        conf.job_started = True
    conf.transform_started = 'LANDING_JSON' in os.listdir(conf.job_destination)
    for game_data in conf.file_list:
        data_table = conf.file_list[game_data]
        for data_file in data_table["file_list"]:
            file_origin = f'{conf.file_origin}{data_table["directory_path"]}/{data_file["file_name"]}'
            file_name = f'{data_file["file_name_alias"] if "file_name_alias" in data_file else data_file["file_name"]}'
            copy(file_origin, f'{conf.job_destination}/{file_name}')
    if not conf.transform_started:
       os.mkdir(conf.db_load_source)
       conf.transform_started = True

# prepare_files()
