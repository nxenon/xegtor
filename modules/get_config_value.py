#!/usr/bin/env python3


'''
this module is for reading GUI/config.json file and return value for desired key
'''

import json

def get_config_value(main_key,key_in_list=None):
    file = open('GUI/config.json')
    config_file = json.load(file)
    try :
        if key_in_list :
            value = config_file[main_key][0][key_in_list]
        else:
            value = config_file[main_key][0]
    except :
        print('Error finding : ' + main_key + ' --> ' + key_in_list)
    else:
        return value