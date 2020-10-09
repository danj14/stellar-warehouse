import xml.etree.ElementTree as eTree
# TODO method for retrieving values:
# - Inputs:
#   * file_list.json as JSON object
#   * flat_schema.json as JSON object (adjusted top-most of each table to use table alias)
#   * staging directory info
# - Outputs:
#   * JSON representation of the EXML data according to the schema file

class TransformGameFiles:
    def __init__(self, file_list={}, file_schema={}, stage=''):
        self.file_list = file_list
        self.file_schema = file_schema
        self.stage = stage
        self.file_root = None
        self.set_schema = None
        self.landing_table = None

    def file_spotlight(self, file=None, landing_table=None):
        parsed_file = eTree.parse(f'{self.stage}/{file}')
        self.file_root = parsed_file.getroot()
        self.set_schema = self.file_schema["table"][landing_table]
        self.landing_table = landing_table

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
                            for target_attribute in schema_info["ingredients"]:
                                ingredient_object[target_attribute["attribute_name"]] = ingredient.find(
                                    f'{target_attribute["cursor"]}').get(target_attribute["key"])
                        group_attributes.append(ingredient_object)
                    data_object[schema_info["field_name"]] = group_attributes
                    data_object[schema_info["group_key"]] = "True" if len(group_attributes) > 0 else "False"
                else:
                    data_object[schema_info["field_name"]] = top_level.find(f'{schema_info["cursor"]}')\
                        .get(schema_info["key"])
            file_items.append(data_object)
        return {self.landing_table: file_items}
