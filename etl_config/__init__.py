import os
import json
from datetime import date

__all__ = ['queries']

def prepare_configuration(message):
    if not job_started:
        print('Runtime directory has not been created.')
        exit(code=-1)
    if not transform_started:
        print('JSON directory for DB loading has not been created.')
        exit(code=-1)
    print(f'Runtime directories present...running {message}')

def open_file_to_json(file):
    # TODO: Pass in a few shit objects of different types; how does this break?
    with open(file, 'r') as f:
        file_data = f.read()
    return json.loads(file_data)

# maybe we can use YAML or something instead? treat it as true config

# module path
f_path = os.path.dirname(os.path.realpath(__file__)).replace('\\','/')

# file loading parameters
mapping_schema = open_file_to_json(f'{f_path}/extract_mapping_schema.json')
file_list = open_file_to_json(f'{f_path}/file_list.json')
file_origin = os.environ["DEV_FILE_ORIGIN"]
file_destination = os.environ["DEV_FILE_DESTINATION"]

# job run parameters
job_label = f'{date.today().strftime("%Y.%m.%d")}-NMS_Source'
job_destination = f'{file_destination}/{job_label}'
job_started = job_label in os.listdir(file_destination)
job_files = os.listdir(job_destination) if job_started else []


# extraction destination/landing
db_load_source = f'{job_destination}/LANDING_JSON'
db_copy_source = f'{job_destination}/LANDING_CSV'
db_load_queue = os.listdir(db_load_source) if job_started else []
db_load_source_check = lambda f: f in db_load_queue
transform_started = 'LANDING_JSON' in job_files
copy_loading_started = 'LANDING_CSV' in job_files

# logging and other end tasks
job_end = f'===END==={job_label}.json'
# TODO: refactor to check for "finish" file once that is implemented
job_finished = job_started and job_end in os.listdir(file_destination)
