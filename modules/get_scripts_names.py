#!/usr/bin/env python3

'''
this module returns scripts names
'''

def get_scripts_names():
    contents = ''
    with open('scripts/scripts_names.txt', 'r') as s_file:
        content = s_file.read()
        return content