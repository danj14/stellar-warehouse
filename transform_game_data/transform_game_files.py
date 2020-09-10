import xml.etree.ElementTree as eTree
# TODO method for retrieving values:
# - Inputs:
#   * file_list.json as JSON object
#   * flat_schema.json as JSON object
#   * staging directory info
# - Outputs:
#   * JSON representation of the EXML data according to the schema file

class TransformGameFiles:
    def __init__(self, file_list={}, file_schema={}, stage=''):
        self.file_list = file_list
        self.file_schema = file_schema
        self.stage = stage
        self.file_root = None

    def file_spotlight(self, file=None):
        # open exml file
        # initiate exml root
        # set instance variable to exml root
        parsed_file = eTree.parse(f'{self.stage}/{file}')
        self.file_root = parsed_file.getroot()

    def render_json(self):
        print(f'{self.file_root}')
