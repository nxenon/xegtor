#!/usr/bin/env python3

'''
this script is for /perform_attack page in which you can perform and start attack
'''

from flask import render_template,request,redirect
import json
from modules.get_argument_default_value import get_default_value
from main.core.script_mgr import ScriptManager
from threading import Thread

def run_attack(script_name,arguments_dict):
    script_manager = ScriptManager(script_name=script_name ,gui_args=arguments_dict)
    Thread(target=script_manager.run_script).start()

def show_arguments():
    content = ''
    file = open('GUI/functions/arguments.json', 'r')
    arguments_in_file = json.load(file)
    script_name = request.args.get('script')
    content += '<h2 class="text-center">' + script_name + '</h2></div>' # show script name in top of the page

    url_args_names = list(request.args)
    content += '''
    <div class="card-body">
        <div class="my-3">
    '''
    arguments_and_values = {} # store arguments and their values into a dictionary to pass in run_attack function
    for arg in url_args_names :
        if arg != 'script' :
            argument_value = request.args.get(arg)
            if argument_value == '':
                default_value = get_default_value(script_name=script_name ,argument=arg)
                argument_value = default_value[1]

            content += '<h4 style="text-align : center">' + arg + ' : ' + argument_value + '</h4>'
            arguments_and_values[arg.lower()] = argument_value
    content += '''
    </div>
    '''
    try:
        run_attack(script_name=script_name, arguments_dict=arguments_and_values)
    except Exception:
        pass
    return content, script_name

def perform_attack():
    page = render_template('stream_log.html')
    if (request.cookies.get('logged_in') == 'yes'):
        page = page.replace('{to_replace_username}', request.cookies.get('user').title())
    else:
        return redirect('/login', code=302)

    content, script_name = show_arguments()
    page = page.replace('{script_name}', script_name) # Replace name of the script has been run in template
    page = page.replace('{to_replace_text}', content)
    return page