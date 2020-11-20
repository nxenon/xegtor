#!/usr/bin/env python3

'''
this module is for checking if the script argument is required or not
it returns True or False (True if the argument is required)
'''

import json

file = open('GUI/functions/arguments.json','r')
arguments_in_file = json.load(file)

def argument_is_required(script_name,argument):
    script_args = arguments_in_file[script_name][0]
    if (script_args[argument] == '*') : # * means the argument is required
        return True
    else:
        return False