import os
import json
from extract_game_data import stage_game_files as stg
from transform_game_data import transform_game_files as transformer
from transform_game_data import load_game_files as loader

# TODO: we are doing a lot of file opening...
# TODO: create runtime config class?
# TODO: Memory leak somewhere in looking through directories; leaving the path open and causing a permission error


"""

Rough idea of project structure for packages...

custom packages <-- thinking about publishing for others figure out how to place with other packages?:

    pgpy_lite/
        __init__.py
        cast_params.py
        transpose_query.py
        
    nms_xml/
        __init__.py
        # modules for transforming nsm xml data to json representation

pipelines structure; I think we stick w/class based for any core activities that require persistence

/
    [1] prepare_files.py
    [2] extract.py
    [3] transform.py
    [4] load.py

not all of these need to be packages
etl_config/
    __init__.py
    queries/
        __init__.py
        admin/
            create_product_landing.sql
            create_product_ingredient_landing.sql
            # TODO: drop_product_landing.sql
            # TODO: drop_product_ingredient_landing.sql
        landing/
            __init__.py
            load_product.sql
            load_product_ingredient.sql
    file_list.json
    extract_schema.json
    

landing/
    __init__.py
    extract.py
    transform.py
    load.py

staging/

MILESTONES
    [1] complete data loading to landing tables
    [2] complete data loading to staging tables
    [3] complete data loading to presentation tables
    [4] decide which charts/features to demonstrate
    [5] publish initial site to share stuff from #4

REFACTOR ORDER
    **DONE** [1] create "prepare_files.py" under the main runtime directory (research what this might be?)
    [2] create whichever files will extract data from the exml and translate it to json and write to "disk"
    [3] create whichever files will transform and load the JSON data previously written to "disk"
    [4] create whichever files will extract landing data and transform and load to staging tables
    [5] create whichever files will load staging table data, do indexes and such to presentation tables


"""

def stage_game_files():
    origin = os.environ['DEV_FILE_ORIGIN']
    destination = os.environ['DEV_FILE_DESTINATION']
    file_list_config = open('extract_game_data/game_data_extract_config/file_list.json', 'r')
    file_list = file_list_config.read()
    file_list_config.close()
    file_list = json.loads(file_list)

    # TODO: Refactor stage game class to be  file handler



    staged_files = stg.StageGameFiles(file_list, origin, destination)

    if staged_files.check_for_stage(staged_files.destination_parent_path, staged_files.current_extraction_run):
        staged_files.clear_stage(staged_files.staging_path)
    staged_files.create_stage(staged_files.staging_path)
    stage = staged_files.bring_to_stage()
    return {"file_config_json": file_list, "stage": stage}

def transform_game_files():
    with open('extract_game_data/game_data_extract_config/flat_schema.json', 'r') as configs:
        config_data = configs.read()
    schema_config = json.loads(config_data)
    staged_game_files = stage_game_files()


    # TODO: rename "start_d"
    start_d = transformer.TransformGameFiles(staged_game_files["file_config_json"], schema_config, staged_game_files["stage"])
    # TODO: replace with loop/crawler to go through all files


    start_d.file_spotlight(staged_game_files["file_config_json"]["reality_tables"]["file_list"][0]["file_name"],
                           staged_game_files["file_config_json"]["reality_tables"]["file_list"][0]["landing_tables"][0])
    temp_debug_json = start_d.render_json()
    destination_parent_path = os.environ['DEV_FILE_DESTINATION']
    stage = stg.StageGameFiles(destination_parent_path=destination_parent_path)

    if stage.check_for_stage(stage.staging_path, 'JSON_STAGE'):
        stage.clear_stage(f'{stage.staging_path}/JSON_STAGE')
    stage.create_stage(f'{stage.staging_path}/JSON_STAGE')
    file_destination = f'{stage.staging_path}/JSON_STAGE/' \
                       f'{staged_game_files["file_config_json"]["reality_tables"]["file_list"][0]["landing_tables"][0]}' \
                       f'.json'
    land_file = open(file_destination, 'w')
    json.dump(temp_debug_json, land_file, indent=4)
    land_file.close()
    return temp_debug_json

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


print('==================== RAW OUTPUTS ====================')
g_staged_game_files = stage_game_files()
print('******************** Stage game files ********************')
print(f'{g_staged_game_files["file_config_json"]}')
print(f'{g_staged_game_files["stage"]}')
print('******************** Transform game files ********************')
load_game_files(transform_game_files())



"""
Background:
--ref: https://nmsmodding.fandom.com/wiki/Getting_Started --
* Files: V:\\\\SteamLibrary\\\\steamapps\\\\common\\\\No Man's Sky\\GAMEDATA\\PCBANKS
* Extract using... C:\\Users\\Dan\\Documents\\Projects\\PSArcTool
* Extract MBIN for applicable files to EXML...C:\\Users\\Dan\\Documents\\Projects\\MBINCompiler.exe

Goals:
1) Optimize value per <x> time period for farming
-> trading and economy information will likely be very valuable to min/max farming output + sale
2) Optimize value per base size for farming (maybe combo w/#1)


Files needed:
    Directory: N:/NMS Game Files/METADATA/REALITY/TABLES
        / TRADINGCOSTTABLE.EXML
        / TRADINGCLASSDATATABLE.EXML
        / NMS_REALITY_GC_PRODUCTTABLE.EXML
        / COSTTABLE.EXML
        / NMS_REALITY_GCSUBSTANCETABLE.EXML
    Direcotry: N:/NMS Game Files/METADATA/LANGUAGE
        / NMS_LOC1_ENGLISH.EXML
        / NMS_LOC4_ENGLISH.EXML
        / NMS_LOC5_ENGLISH.EXML
        / NMS_LOC6_ENGLISH.EXML
        / NMS_UPDATE3_ENGLISH.EXML
        / NMS_UPDATE3_USENGLISH.EXML
        # <*>_<NAME/ID>_NAME_L

-- side thing --
/ NMS_DIALOG_GCALIENPUZZLETABLE.EXML
/ NMS_DIALOG_GCALIENSPEECHTABLE.EXML

Pipeline:
TODO: create initial parsing script for a table; identify possible parameters
TODO: create config design for parameterizing by file for how XML needs to be parsed
TODO: loop through target files, converting data to .csv
TODO: load .csv to PostgreSLQ DB

# Design NMS Data Warehouse
# Enforce FK/PK relationships on load

TRADINGCOSTTABLE.EXML
# Only need to focus on [2] parent node <Doc Parent> ==> <Redundant Parent> ==> <Item "record"> ==> <Item details>



~~====NMS_REALITY_GC_PRODUCTTABLE.EXML====~~
###need refactor
import xml.etree.ElementTree as et
xml_file = et.parse(<file path>)
root = xml_file.getroot()
true_root = root[0]

some_dict = {}
... for node in true_root:
...     dict_id = ''
...     attrib_pairs = {}
...     i = 0
...     for prop in node.iter('Property'):
...         if 'name' in prop.attrib and 'value' in prop.attrib and prop.attrib['name'] in all_attributes:
...             if prop.attrib['name'] == 'Id':
...                 dict_id = prop.attrib['value']
...                 some_dict[prop.attrib['value']] = {}
...             else:
...                 if prop.attrib['name'] in some_dict[dict_id]:
...                     some_dict[dict_id][f'{prop.attrib["name"]}_alt{i}'] = prop.attrib['value']
...                     i += 1
...                 else:
...                     some_dict[dict_id][prop.attrib['name']] = prop.attrib['value']
...         else:
...             continue

NEXT: update dict so that requirements are in an array of key/value pairs rather than a flat list of elements?
or use this:

true_root[0].findall(".//Property/[@name='Requirements']")[0].attrib
{'name': 'Requirements'}
true_root[0].findall(".//Property/[@name='Requirements']*/Property/[@name='ID']")[0].attrib
"""