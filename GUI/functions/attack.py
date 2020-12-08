#!/usr/bin/env python3

'''
this script is for /attack page in which you can start attacks
'''

from flask import render_template,request,redirect
import json
from modules.check_required_argument import argument_is_required
from modules.get_argument_default_value import get_default_value

def show_options(script):
    option_text = '<br><br><h2 style="text-align : center">' + script + '</h2><br><br>'
    option_text += '''
    <form action="/perform_attack" method="get">
    <div style="text-align : center">
    <h2>Arguments</h2><br>
    '''
    option_text += '<input type="hidden" name="script" value="' + script + '"'

    file = open('GUI/functions/arguments.json','r')
    arguments_in_file = json.load(file)
    for script_args in arguments_in_file[script] :
        args_list = list(script_args.keys())
        for arg in args_list :
            if arg != 'log_name' : # ignore log name in arguments.json
                if (argument_is_required(script_name=script,argument=arg)) :
                    option_text += '<label>' + arg.title() + ' </label>'
                    option_text += '<input style="font-size : 25px" type="text" placeholder="Enter ' + arg.title() + '"' + 'name="' + arg + '" required><br><br>'
                else:
                    option_text += '<label>' + arg.title() + ' </label>'
                    option_text += '<input style="font-size : 25px" type="text" placeholder="' + get_default_value(script_name=script,argument=arg)[0].title() + '"' + 'name="' + arg + '"><br><br>'

    option_text += '''<br>
    <button class="button-attack">Start</button>
    </div>
    </form>
    <h3 style="text-align : center"><a href="/show_examples" target="_blank">Show Examples</a></h3>
    '''

    return option_text

def attack():
    page = render_template('dashboard.html')
    if (request.cookies.get('logged_in') == 'yes'):
        page = page.replace('{to_replace_username}', request.cookies.get('user').title())
    else:
        return redirect('/login', code=302)

    if not (request.args.get('script')) : # if script argument is not set
        page = page.replace('{to_replace_text}','<h1 style="text-align : center">Choose a script ---> <a href="/scripts"> script page</a></h1>')
        return page
    else:
        chosen_script = request.args.get('script')
        texts = show_options(script=chosen_script)
        page = page.replace('{to_replace_text}',texts)
        return page