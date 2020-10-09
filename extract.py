


"""
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

"""