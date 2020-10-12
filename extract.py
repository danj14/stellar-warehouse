import etl_config as conf
import nms_xml as nms
import json

def extract_files():
    conf.prepare_configuration(__file__)
    xml_file = conf.file_list["reality_tables"]["file_list"][0]["file_name"]
    xml_file_path = conf.job_destination
    file_as_json = nms.xml_to_json(xml_file=f'{xml_file_path}/{xml_file}',
                    json_mapping_schema=conf.mapping_schema["table"]["lnd_d_product"])
    if not conf.db_load_source_check('lnd_d_product.json'):
        with open(f'{conf.db_load_source}/lnd_d_product.json', 'w') as target_file:
            json_file = {"lnd_d_product": file_as_json}
            json.dump(json_file, target_file, indent=4)
    else:
        print('Extract already completed. No JSON created.')

extract_files()


# def for looping through file list (new structure makes this pragmatic)
# TODO: slowly add loop as we build out more file mappings