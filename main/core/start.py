#!/usr/bin/env python3

'''
this script for starting programs function
'''

from main.design.banner import print_banner
from main.design.arg_options import parse_args
from main.design.notes import print_notes

def start():
    print_banner()
    print_notes()
    parse_args()