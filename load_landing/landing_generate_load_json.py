import expected_file_manifest as manifest
import os
import xml.etree.ElementTree as et
from compile_landing_data_dict import landing_dict as landing_dict

print('***************BOM || landing_generate_load.json.py***************\n\n')

data_staging_directory = f'{manifest.destination_parent_path}/{manifest.working_directory[0]}'

print(f'{data_staging_directory}\n')

staging_list = os.listdir(data_staging_directory)
review_path = f'{data_staging_directory}/{staging_list[0]}'
review_file = staging_list[0]
xml_file = et.parse(review_path)
root = xml_file.getroot()
print(f'Reviewing file: {review_path}\n')

# TODO: Objective - open EXML file, refer to schema based on file alias and return JSON matching
confirmed_files = manifest.file_status_list[0]
working_file = [file for file in confirmed_files if file[2] == review_file]
working_file = working_file[0] if len(working_file) == 1 else False
working_file_table = working_file[3] if working_file else False
working_file_table = landing_dict[working_file_table]

xml_target_index = working_file_table['xml_file_root'].split('~')
xml_target_index = {xml_target_index[0]: xml_target_index[1]}
file_root_list = [root_index.attrib for root_index in root]
file_root_index = file_root_list.index(xml_target_index)

print(f'Working table: {working_file_table}')

output_dict = {}


def crawl_xml(value_map=[]):
    for value in value_map:
        parse_properties = seek_index(nav_path=value['nav_path'], nav_anchor=root[file_root_index])
        for prop in parse_properties:
            if value['sought_value_loc'][0] in prop and \
                    prop[value['sought_value_loc'][0]] == value['sought_value_loc'][1]:
                alias = value['dict_alias'] if value['dict_alias'] else value['sought_value_loc'][1]
                output_dict[alias] = prop[value['sought_value_loc'][2]]
            else:
                continue


def seek_index(nav_path=[], nav_anchor=None, depth=0):
    bread_crumbs = [marker.attrib for marker in nav_anchor]
    bread_crumb_match = [marker.attrib for marker in nav_anchor if marker.attrib == nav_path[depth]]
    sub_cursor = 0
    if len(bread_crumb_match) > 1:
        embedded_filter = nav_path[depth + 1]
        for match in bread_crumb_match:
            seeker_index = bread_crumbs.index(nav_path[depth], sub_cursor)
            if embedded_filter in [t.attrib for t in nav_anchor[seeker_index].iter("Property")]:
                return [prop.attrib for prop in nav_anchor[seeker_index].iter('Property')]
            else:
                sub_cursor += 1
    marker_index = bread_crumbs.index(nav_path[depth])
    if len(nav_path) > depth + 1:
        return seek_index(nav_path=nav_path, nav_anchor=nav_anchor[marker_index], depth=depth+1)
    else:
        return [prop.attrib for prop in nav_anchor[marker_index].iter("Property")]


def generate_from_schema():
    value_map = []
    for nav in working_file_table['schema']:
        alias = nav.split('!!')[1] if '!!' in nav else False
        if alias:
            nav = nav.split('!!')[0]
        nav_map = nav.split('>')
        sought_value_loc = nav_map[-1].split('~')
        nav_path = [{sub_nav.split('~')[0]:sub_nav.split('~')[1] for sub_nav in nav_node.split('&&')} if '&&' in
                                                                                                         nav_node
                    else {nav_node.split('~')[0]: nav_node.split('~')[1]} for nav_node in nav_map[:-1]]
        value_map.append({'nav_path': nav_path, 'sought_value_loc': sought_value_loc, 'dict_alias': alias})
    crawl_xml(value_map=value_map)


generate_from_schema()
print(f'{output_dict}')
print('\n\n***************EOM || landing_generate_load.json.py***************\n\n')
