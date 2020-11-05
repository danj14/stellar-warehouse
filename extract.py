import etl_config as conf
import nms_xml as nms
import json

# TODO:
#  this approach feels clumsy to me

def extract_files():
    conf.prepare_configuration(__file__)
    # Configuration
    configured_range = (0, 1)
    configured_landing_table = ('lnd_d_product', 'lnd_d_substance')
    # End Configuration
    for configured_file in configured_range:
        xml_file = conf.file_list["reality_tables"]["file_list"][configured_file]["file_name"]
        file_as_json = nms.xml_to_json(xml_file=f'{conf.job_destination}/{xml_file}',
                                   json_mapping_schema=conf.mapping_schema["table"][
                                       configured_landing_table[configured_file]
                                   ])
        if not conf.db_load_source_check(configured_landing_table[configured_file]):
            with open(f'{conf.db_load_source}/{configured_landing_table[configured_file]}.json', 'w') as target_file:
                json_file = {configured_landing_table[configured_file]: file_as_json}
                json.dump(json_file, target_file, indent=4)
        else:
            print('Extract already completed. No JSON created.')



    # xml_file = conf.file_list["reality_tables"]["file_list"][0]["file_name"]
    # file_as_json = nms.xml_to_json(xml_file=f'{xml_file_path}/{xml_file}',
                                   # json_mapping_schema=conf.mapping_schema["table"]["lnd_d_product"])
    # xml_file_path = conf.job_destination
    # conf.job_files
    #xml_file = conf.file_list["reality_tables"]["file_list"][1]["file_name"]
    #file_as_json = nms.xml_to_json(xml_file=f'{conf.job_destination}/{xml_file}',
    #                               json_mapping_schema=conf.mapping_schema["table"]["lnd_d_substance"])
    #if not conf.db_load_source_check('lnd_d_substance.json'):
    #    with open(f'{conf.db_load_source}/lnd_d_substance.json', 'w') as target_file:
    #        json_file = {"lnd_d_substance": file_as_json}
    #        json.dump(json_file, target_file, indent=4)
    #else:
    #    print('Extract already completed. No JSON created.')
    # if not conf.db_load_source_check('lnd_d_product.json'):
    #     with open(f'{conf.db_load_source}/lnd_d_product.json', 'w') as target_file:
    #         json_file = {"lnd_d_product": file_as_json}
    #         json.dump(json_file, target_file, indent=4)
    # else:
    #     print('Extract already completed. No JSON created.')


extract_files()


# def for looping through file list (new structure makes this pragmatic)
# TODO: slowly add loop as we build out more file mappings