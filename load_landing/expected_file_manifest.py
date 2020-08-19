import os
import re
from datetime import date
from shutil import copy


class OriginDirectory:
    file_home = os.environ['DEV_FILE_ORIGIN']
    destination_parent_path = os.environ['DEV_FILE_DESTINATION']

    def __init__(self, directory_path=None, file_list=[]):
        self.directory_path = directory_path
        self.file_list = file_list

    def full_origin_path(self, file_index=0):
        return f'{self.file_home}{self.directory_path}{self.file_list[file_index]}'


reality_tables = OriginDirectory(directory_path='/METADATA/REALITY/TABLES/',
                                 file_list=[
                                     'NMS_REALITY_GCPRODUCTTABLE.EXML',
                                     'NMS_REALITY_GCSUBSTANCETABLE.EXML',
                                     'TRADINGCLASSDATATABLE.EXML',
                                     'NMS_REALITY_GCRECIPETABLE.EXML'
                                            ])
farming_tables = OriginDirectory(directory_path='/METADATA/LANGUAGE/',
                                 file_list=[
                                     'NMS_LOC1_ENGLISH.EXML',
                                     'NMS_UPDATE3_USENGLISH.EXML',
                                     'NMS_LOC4_ENGLISH.EXML',
                                     'NMS_LOC5_ENGLISH.EXML',
                                     'NMS_LOC6_ENGLISH.EXML'
                                 ])
language_tables = OriginDirectory(directory_path='/MODELS/PLANETS/BIOMES/COMMON/INTERACTIVEFLORA',
                                  file_list=[
                                      '/FARMALBUMEN/ENTITIES/PLANTINTERACTION.ENTITY.EXML',
                                      '/FARMBARREN/ENTITIES/PLANTINTERACTION.ENTITY.EXML',
                                      '/FARMDEADCREATURE/ENTITIES/PLANTINTERACTION.ENTITY.EXML',
                                      '/FARMGRAVITINO/ENTITIES/PLANTINTERACTION.ENTITY.EXML',
                                      '/FARMLUSH/ENTITIES/PLANTINTERACTION.ENTITY.EXML',
                                      '/FARMNIP/ENTITIES/PLANTINTERACTION.ENTITY.EXML',
                                      '/FARMPOOP/ENTITIES/PLANTINTERACTION.ENTITY.EXML',
                                      '/FARMRADIOACTIVE/ENTITIES/PLANTINTERACTION.ENTITY.EXML',
                                      '/FARMSCORCHED/ENTITIES/PLANTINTERACTION.ENTITY.EXML',
                                      '/FARMSNOW/ENTITIES/PLANTINTERACTION.ENTITY.EXML',
                                      '/FARMTOXIC/ENTITIES/PLANTINTERACTION.ENTITY.EXML',
                                      '/FARMVENOMSAC/ENTITIES/PLANTINTERACTION.ENTITY.EXML'
                                  ])
print(language_tables.full_origin_path(1))

print('***************BOM || expected_file_manifest.py***************\n\n')

# Code below not yet in use
########################################################################
files = [
    {
        'file_path': '/METADATA/REALITY/TABLES/',
        'files_to_extract': [
            ('NMS_REALITY_GCPRODUCTTABLE.EXML', {'table_alias': 'nms_product', 'file_alias': 'nms_product'}),
            ('NMS_REALITY_GCSUBSTANCETABLE.EXML', {'table_alias': 'nms_substance', 'file_alias': 'nms_substance'}),
            ('TRADINGCLASSDATATABLE.EXML', {'table_alias': 'nms_trading*', 'file_alias': 'nms_trading'}),
            ('NMS_REALITY_GCRECIPETABLE.EXML', {'table_alias': 'nms_recipe', 'file_alias': 'nms_recipe'})
        ],
        'date_files_last_extracted': [
            None, None, None,
            None
        ]
    },
    {
        'file_path': '/MODELS/PLANETS/BIOMES/COMMON/INTERACTIVEFLORA',
        'files_to_extract': [
            ('PLANTINTERACTION.ENTITY.EXML', {'table_alias': 'farm_plant_table',
                                              'file_alias': 'nms_farm_pearl'}, '/FARMALBUMEN/ENTITIES/'),
            ('PLANTINTERACTION.ENTITY.EXML', {'table_alias': 'farm_plant_table',
                                              'file_alias': 'nms_farm_cactus'}, '/FARMBARREN/ENTITIES/'),
            ('PLANTINTERACTION.ENTITY.EXML', {'table_alias': 'farm_plant_table',
                                              'file_alias': 'nms_farm_mordite'}, '/FARMDEADCREATURE/ENTITIES/'),
            ('PLANTINTERACTION.ENTITY.EXML', {'table_alias': 'farm_plant_table',
                                              'file_alias': 'nms_farm_gravitino'}, '/FARMGRAVITINO/ENTITIES/'),
            ('PLANTINTERACTION.ENTITY.EXML', {'table_alias': 'farm_plant_table',
                                              'file_alias': 'nms_farm_star'}, '/FARMLUSH/ENTITIES/'),
            ('PLANTINTERACTION.ENTITY.EXML', {'table_alias': 'farm_plant_table',
                                              'file_alias': 'nms_farm_bud'}, '/FARMNIP/ENTITIES/'),
            ('PLANTINTERACTION.ENTITY.EXML', {'table_alias': 'farm_plant_table',
                                              'file_alias': 'nms_farm_poop'}, '/FARMPOOP/ENTITIES/'),
            ('PLANTINTERACTION.ENTITY.EXML', {'table_alias': 'farm_plant_table',
                                              'file_alias': 'nms_farm_gamma'}, '/FARMRADIOACTIVE/ENTITIES/'),
            ('PLANTINTERACTION.ENTITY.EXML', {'table_alias': 'farm_plant_table',
                                              'file_alias': 'nms_farm_solar'}, '/FARMSCORCHED/ENTITIES/'),
            ('PLANTINTERACTION.ENTITY.EXML', {'table_alias': 'farm_plant_table',
                                              'file_alias': 'nms_farm_frost'}, '/FARMSNOW/ENTITIES/'),
            ('PLANTINTERACTION.ENTITY.EXML', {'table_alias': 'farm_plant_table',
                                              'file_alias': 'nms_farm_fungal'}, '/FARMTOXIC/ENTITIES/'),
            ('PLANTINTERACTION.ENTITY.EXML', {'table_alias': 'farm_plant_table',
                                              'file_alias': 'nms_farm_venom'}, '/FARMVENOMSAC/ENTITIES/')
        ],
        'date_files_last_extracted': [
            None, None, None,
            None, None, None,
            None, None, None,
            None, None, None
        ]
    },
    {
        'file_path': '/METADATA/LANGUAGE/',
        'files_to_extract': [
            ('NMS_LOC1_ENGLISH.EXML', {'table_alias': 'nms_language', 'file_alias': 'nms_language1'}),
            ('NMS_UPDATE3_USENGLISH.EXML', {'table_alias': 'nms_language', 'file_alias': 'nms_language3'}),
            ('NMS_LOC4_ENGLISH.EXML', {'table_alias': 'nms_language', 'file_alias': 'nms_language4'}),
            ('NMS_LOC5_ENGLISH.EXML', {'table_alias': 'nms_language', 'file_alias': 'nms_language5'}),
            ('NMS_LOC6_ENGLISH.EXML', {'table_alias': 'nms_language', 'file_alias': 'nms_language6'})
        ],
        'date_files_last_extracted': [
            None, None, None,
            None, None
        ]
    }
]
api_sources = []


def make_extraction_destination_directory():
    past_extractions = os.listdir(destination_parent_path)
    new_directory = f'{date.today().strftime("%Y.%m.%d")}-NMS_Source'
    # TODO: need to come back to gracefully handle this...
    execute_copy = False
    if new_directory not in past_extractions:
        os.makedirs(f'{destination_parent_path}/{new_directory}')
        execute_copy = 1
        print('success: directory created')
    else:
        execute_copy = 0
        print('warning: source destination directory already exists')
    return new_directory, execute_copy


def copy_source_files(source, alias):
    destination = f'{destination_parent_path}/'
    copy(source, f'{destination}/{alias}')
    # TODO: file check after all copying for expected files


def file_manifest():
    found_file_list = []
    missing_file_list = []
    for file_set in files:
        expected_files = [f[0] for f in file_set['files_to_extract']]
        sub_dirs = [f[2] for f in file_set['files_to_extract'] if len(f) > 2]
        files_in_directory = []
        if len(sub_dirs) > 0:
            staged_files = []
            for s_path in sub_dirs:
                directory_files = os.listdir(f'{file_home}{file_set["file_path"]}{s_path}')
                staged_files.extend((file, file_set['file_path'] + s_path) for file in directory_files)
            files_in_directory.extend(staged_files)
            files_found = [(f[0], file_set['file_path'] + f[2], f'{f[1]["file_alias"]}.EXML', f[1]["table_alias"]) for f
                           in file_set['files_to_extract'] if (f[0], file_set['file_path'] + f[2])
                           in files_in_directory]
            files_missing = [(f[0], file_set['file_path'] + f[2]) for f in file_set['files_to_extract'] if
                             (f[0], file_set['file_path'] + f[2]) not in files_in_directory]
        else:
            directory_files = os.listdir(f'{file_home}{file_set["file_path"]}')
            files_in_directory.extend([(file, file_set['file_path']) for file in directory_files])
            files_found = [(file[0], file_set["file_path"], f'{file[1]["file_alias"]}.EXML', file[1]["table_alias"])
                           for file in file_set['files_to_extract']
                           if (file[0], file_set["file_path"]) in files_in_directory]
            files_missing = [(file[0], file_set["file_path"]) for file in file_set['files_to_extract'] if
                             (file[0], file_set["file_path"]) not in files_in_directory]
        found_file_list.extend(files_found)
        missing_file_list.extend(files_missing)
    return found_file_list, missing_file_list


# working_directory = make_extraction_destination_directory()
# file_status_list = file_manifest()
"""
print('Files found: ')
for located in file_status_list[0]:
    print(f'{located[1]}..... {located[0]}\n')
    if working_directory[1] and working_directory[1] == 1:
        copy(f'{file_home}{located[1]}{located[0]}', f'{destination_parent_path}/{working_directory[0]}/{located[2]}')
        if located[2] in os.listdir(f'{destination_parent_path}/{working_directory[0]}'):
            print(f'success: {located[0]} copied as "{located[2]}"')
        else:
            print(f'error: {located[0]} failed to copy to destination!')
    else:
        print(f'Files may already exist; not copying...{located[0]}')
print('Files missing: ')
for missing in file_status_list[1]:
    print(f'{missing[1]}..... {missing[0]}\n')
"""

print('\n\n***************EOM || expected_file_manifest.py***************\n\n')
