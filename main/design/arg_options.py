#!/usr/bin/env python3

import re
import argparse
from sys import argv

scripts_name_all = [] # this list contains all of scripts name for existence checking in --script script_name parameter

def parse_args():
    parser = argparse.ArgumentParser(usage='sudo python3 %(prog)s --script script_name [options]' + '\n help: sudo python3 %(prog)s --help' + '\n  GUI: sudo python3 %(prog)s --gui')
    parser.add_argument('--gui',help='Start GUI Web Interface',action='store_true')
    parser.add_argument('--script',help='Script Name To Choose',metavar='script_name')
    parser.add_argument('--show-scripts',help='Show Scripts Names',action='store_true')
    parser.add_argument('--show-examples',help='Show Some Examples',action='store_true')

    args ,unknown = parser.parse_known_args()

    # check argument passed
    if (args.gui):
        import GUI.main
        return
    elif ((args.script is not None) and (args.script in scripts_name_all)):
        send_script(script_name=args.script) # send to process script

    elif ((args.script is not None) and (args.script not in scripts_name_all)) :
        print('Invalid script name ---> --help for help')
    else:
        parser.print_usage()
        print()

    if args.show_scripts :
        show_scripts_names()
    if args.show_examples :
        show_examples()

def add_scripts_names():
    '''this function adds scripts names to scripts_name_all list and will be called at first'''
    file_regex = '''(.*):::(.*)'''  # regex for scripts_names.txt file
    with open('scripts/scripts_names.txt', 'r') as s_file:
        content = s_file.read()
        scripts_list = re.findall(file_regex, content)  # data format [(script_name,script_description)]
        for s in scripts_list:
            scripts_name_all.append(s[0])

def show_examples():
    examples_prefix = 'sudo python3 ' + argv[0] + ' ' # prefix for every example read from examples.txt file
    examples_lines_list = [] # lines written from examples.txt
    with open('scripts/examples.txt','r') as e_file :
        examples_lines_list = e_file.readlines()

    print('Examples :')
    for e in examples_lines_list :
        if e.startswith('#'): # title of examples.txt file
            pass
        elif e.startswith('['): # every line that starts with [ is script name not example
            print(e,end='')
        else:
            print(examples_prefix + e ,end='')
    print()

def show_scripts_names():
    file_regex = '''(.*):::(.*)''' # regex for scripts_names.txt file
    scripts_dict = {} # dictionary for scripts names and their description
    print('Scripts Names :')
    with open('scripts/scripts_names.txt','r') as s_file :
        content = s_file.read()
        scripts_list = re.findall(file_regex,content) # data format [(script_name,script_description)]
        for s in scripts_list :
            scripts_dict[s[0]] = s[1]

    for s_name,s_desc in scripts_dict.items() :
        print('name : ' + s_name + ' ---> ' + s_desc)

def send_script(script_name):
    from main.core import script_mgr
    script_mgr =  script_mgr.ScriptManager(script_name=script_name)
    script_mgr.run_script()

add_scripts_names() # for adding scripts name into scripts_name_all list