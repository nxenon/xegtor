#!/usr/bin/env python3

'''
this module returns the default value for the argument if the argument has (a default value) and (is not required)
'''

import json

file = open('GUI/functions/arguments.json','r')
arguments_in_file = json.load(file)

def get_default_value(script_name,argument):
    script_args = arguments_in_file[script_name][0]
    default_value = script_args[argument][1]
    return default_value