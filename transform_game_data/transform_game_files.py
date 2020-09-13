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

    def file_spotlight(self, file=None, landing_table=None):
        parsed_file = eTree.parse(f'{self.stage}/{file}')
        self.file_root = parsed_file.getroot()
        self.set_schema = self.file_schema["table"][landing_table]

    def render_json(self):
        arr_r = []
        for top_level in self.file_root.iterfind(f'{self.set_schema["block_value"]}'):
            data_object = {}
            for schema_info in self.set_schema["table_schema"]:
                if "is_group" in schema_info and schema_info["is_group"]:
                    group_attributes = []
                    for sub_level in top_level.iterfind(f'{schema_info["group_block"]}'):
                        ingredient_object = {}
                        #print(sub_level.find(".//*/[@name='ID']").get("value"))
                        for ingredient in sub_level.iterfind(f'{schema_info["ingredient_block"]}'):
                            print(sub_level.find(".*/[@name='ID']").attrib)
                            ingredient_object[schema_info[]]
                    data_object[schema_info["field_name"]] = group_attributes
                else:
                    data_object[schema_info["field_name"]] = top_level.find(f'{schema_info["cursor"]}')\
                        .get(schema_info["key"])
            arr_r.append(data_object)
            # print(top_level.find(".*/Property/[@name='Requirements']").get("value"))
        return ''
