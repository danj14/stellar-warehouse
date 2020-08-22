import os
from shutil import copy, rmtree
from datetime import date

# TODO: Document scope of module
#       Input: file_list.json [Done]
#       Input: physical files and their origin [Done]
#       Output: files moved to staging directory [Done]
#       Output: log file of when this started and ended and each file's copy progress

# TODO: Implement resume functionality for failed jobs?

class StageGameFiles:
    def __init__(self, config_json={}, file_home='', destination_parent_path=''):
        self.config_json = config_json
        self.file_home = file_home
        self.destination_parent_path = destination_parent_path
        self.current_extraction_run = f'{date.today().strftime("%Y.%m.%d")}-NMS_Source'
        self.staging_path = f'{self.destination_parent_path}/{self.current_extraction_run}'

    def check_for_stage(self):
        past_extractions = os.listdir(self.destination_parent_path)
        new_extraction = self.current_extraction_run
        return new_extraction in past_extractions

    def create_stage(self):
        os.makedirs(self.staging_path)

    def clear_stage(self, stage_debug):
        if stage_debug:
            print('Directory will be deleted in prod run...')
        else:
            rmtree(f'{self.staging_path}')

    def bring_to_stage(self):
        absolute_file_paths = []
        for file_group in self.config_json:
            file_group = self.config_json[file_group]
            file_group_path = f'{self.file_home}{file_group["directory_path"]}'
            absolute_file_paths.extend([{"path": f'{file_group_path}/{file["file_name"]}',
                                        "alias": file["file_name_alias"] if "file_name_alias" in file
                                        else file["file_name"]} for file in file_group["file_list"]])
        for file in absolute_file_paths:
            copy(file["path"], f'{self.staging_path}/{file["alias"]}')

