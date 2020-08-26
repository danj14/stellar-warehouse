# TODO method for retrieving values: 
# - Inputs:
#   * EXML root cursor and open stream? (or file stream in mem?) 
#   * Config objects to loop through w/schema cursor info
# - Outputs:
#   * JSON representation of the EXML data according to the config file; JSON { LIST [ JSON{} ] }

def something():
    # FOLLOW THE TREES/ROOTS
    hh_json_confg_simp = 'bee:aee=>c'
    hh_json_config_thot = 'bee:aee=>:c=>a,b,c'
    hh_json_config_list = []
    xml_cursor_index = 0
    xml_root = []

