import xml.etree.ElementTree as eTree
import etl_config as conf

def xml_root(xml_file):
    parsed_file = eTree.parse(xml_file)
    return parsed_file.getroot()


def xml_to_json(xml_file, json_mapping_schema):
    xml_items_as_json = []
    for xml_object in xml_root(xml_file).iterfind(json_mapping_schema["block_value"]):
        json_object = {}
        for target_attribute in json_mapping_schema["mapping_schema"]:
            if "group_key" in target_attribute and "is_group" in target_attribute and target_attribute["is_group"]:
                group_items = []
                for attribute_group in xml_object.iterfind(target_attribute["group_block"]):
                    group_item_object = {}
                    for group_item_cursor in attribute_group.iterfind(target_attribute["group_list_block"]):
                        for group_item in target_attribute["group_list"]:
                            group_item_object[group_item["attribute_name"]] = group_item_cursor\
                                .find(group_item["cursor"]).get(group_item["key"])
                    group_items.append(group_item_object)
                json_object[target_attribute["attribute_name"]] = group_items
                json_object[target_attribute["group_key"]] = "True" if len(group_items) > 0 else "False"
            else:
                json_object[target_attribute["attribute_name"]] = xml_object.find(target_attribute["cursor"])\
                    .get(target_attribute["key"])
        xml_items_as_json.append(json_object)
    return xml_items_as_json

"""

def render_json(self):
    file_items = []
    for top_level in self.file_root.iterfind(f'{self.set_schema["block_value"]}'):
    
    
        data_object = {}
        
        
        for schema_info in self.set_schema["table_schema"]:
            if "is_group" in schema_info and schema_info["is_group"]:
                group_attributes = []
                for sub_level in top_level.iterfind(f'{schema_info["group_block"]}'):
                    ingredient_object = {}
                    for ingredient in sub_level.iterfind(f'{schema_info["ingredient_block"]}'):
                    <== now subgroup block
                        for target_attribute in schema_info["ingredients"]:
                        <== no called "list"
                            ingredient_object[target_attribute["attribute_name"]] = ingredient.find(
                                f'{target_attribute["cursor"]}').get(target_attribute["key"])
                    group_attributes.append(ingredient_object)
                data_object[schema_info["field_name"]] = group_attributes
                data_object[schema_info["group_key"]] = "True" if len(group_attributes) > 0 else "False"
            else:
                data_object[schema_info["field_name"]] = top_level.find(f'{schema_info["cursor"]}') \
                    .get(schema_info["key"])
        
        
        file_items.append(data_object)
    return {self.landing_table: file_items}
"""