import os
import json
from datetime import date

def open_file_to_json(file):
    # TODO: Pass in a few shit objects of different types; how does this break?
    with open(file, 'r') as f:
        file_data = f.read()
    return json.loads(file_data)

f_path = os.path.dirname(os.path.realpath(__file__)).replace('\\','/')

mapping_schema = open_file_to_json(f'{f_path}/extract_mapping_schema.json')
file_list = open_file_to_json(f'{f_path}/file_list.json')
file_origin = os.environ["DEV_FILE_ORIGIN"]
file_destination = os.environ["DEV_FILE_DESTINATION"]
job_label = f'{date.today().strftime("%Y.%m.%d")}-NMS_Source'
job_destination = f'{file_destination}/{job_label}'
job_started = job_label in os.listdir(file_destination)
job_end = f'===END==={job_label}.json'
# TODO: refactor to check for "finish" file once that is implemented
job_finished = job_started and job_end in os.listdir(file_destination)
