#!/usr/bin/env python3

'''
this script is for /perform_attack page in which you can perform and start attack
'''

from flask import render_template,request,redirect
import json
from modules.get_argument_default_value import get_default_value
from main.core.script_mgr import ScriptManager

def run_attack(script_name,arguments_dict):
    script_manager = ScriptManager(script_name=script_name ,gui_args=arguments_dict)
    script_manager.run_script()

def show_arguments():
    content = ''
    file = open('GUI/functions/arguments.json', 'r')
    arguments_in_file = json.load(file)
    script_name = request.args.get('script')
    content += '<br><br><h2 style="text-align : center">' + script_name + '</h2>' # show script name in top of the page

    url_args_names = list(request.args)
    content += '<br><br>'
    arguments_and_values = {} # store arguments and their values into a dictionary to pass in run_attack function
    for arg in url_args_names :
        if arg != 'script' :
            argument_value = request.args.get(arg)
            if argument_value == '':
                default_value = get_default_value(script_name=script_name ,argument=arg)
                argument_value = default_value[1]

            content += '<h4 style="text-align : center">' + arg + ' : ' + argument_value + '</h4>'
            arguments_and_values[arg.lower()] = argument_value

    content += '<br><br>'
    run_attack(script_name=script_name ,arguments_dict=arguments_and_values)
    return content

def perform_attack():
    page = render_template('dashboard.html')
    if (request.cookies.get('logged_in') == 'yes'):
        page = page.replace('{to_replace_username}', request.cookies.get('user').title())
    else:
        return redirect('/login', code=302)

    content = show_arguments()
    page = page.replace('{to_replace_text}',content)
    return page