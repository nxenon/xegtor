#!/usr/bin/env python3

'''
this scripts checks os information
'''

import sys

def what_is_os():
    platform = sys.platform
    if platform == 'win32':
        return 'windows'
    elif platform == 'linux' :
        return 'linux'