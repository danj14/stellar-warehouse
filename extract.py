import etl_config as conf
import nms_xml as nms

# HOLD UP! Shy code, Danno!

def extract_files():
    if not conf.job_started:
        print('Runtime directory has not been created.')
        exit(code=-1)
    # for loop through file_list
    xml_file = conf.file_list["reality_tables"]["file_list"][0]["file_name"]
    xml_file_path = conf.job_destination
    file_as_json = nms.xml_to_json(xml_file=f'{xml_file_path}/{xml_file}',
                    json_mapping_schema=conf.mapping_schema["table"]["lnd_d_product"])
    print(file_as_json)
    # bookmark: next we are working on saving the file to {file_as_json} a .json file then moving on to loading data to landing



extract_files()


# def for looping through file list (new structure makes this pragmatic)
# probably should check that directory we are extracting from exists

"""
# next step is to open files and eTree.parse


def file_spotlight(self, file=None, landing_table=None):
        parsed_file = eTree.parse(f'{self.stage}/{file}')
        self.file_root = parsed_file.getroot()
        self.set_schema = self.file_schema["table"][landing_table]
        self.landing_table = landing_table


mapping_schema replaced table_schema



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




if stage.check_for_stage(stage.staging_path, 'JSON_STAGE'):
        stage.clear_stage(f'{stage.staging_path}/JSON_STAGE')
    stage.create_stage(f'{stage.staging_path}/JSON_STAGE')
    file_destination = f'{stage.staging_path}/JSON_STAGE/' \
                       f'{staged_game_files["file_config_json"]["reality_tables"]["file_list"][0]["landing_tables"][0]}' \
                       f'.json'
    land_file = open(file_destination, 'w')
    json.dump(temp_debug_json, land_file, indent=4)
    land_file.close()


def transform_game_files():
    with open('extract_game_data/game_data_extract_config/flat_schema.json', 'r') as configs:
        config_data = configs.read()
    schema_config = json.loads(config_data)
    staged_game_files = stage_game_files()
    [DON'T NEED]


    # TODO: rename "start_d"
    start_d = transformer.TransformGameFiles(staged_game_files["file_config_json"], schema_config, staged_game_files["stage"])
    # TODO: replace with loop/crawler to go through all files


    start_d.file_spotlight(staged_game_files["file_config_json"]["reality_tables"]["file_list"][0]["file_name"],
                           staged_game_files["file_config_json"]["reality_tables"]["file_list"][0]["landing_tables"][0])
    temp_debug_json = start_d.render_json()
    destination_parent_path = os.environ['DEV_FILE_DESTINATION']
    stage = stg.StageGameFiles(destination_parent_path=destination_parent_path)


    return temp_debug_json


    def __init__(self, file_list={}, file_schema={}, stage=''):
        self.file_list = file_list
        self.file_schema = file_schema
        self.stage = stage
        self.file_root = None
        self.set_schema = None
        self.landing_table = None





"""