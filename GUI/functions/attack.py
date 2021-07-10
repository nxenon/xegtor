#!/usr/bin/env python3

'''
this script is for /attack page in which you can start attacks
'''

from flask import render_template,request,redirect
import json
from modules.check_required_argument import argument_is_required
from modules.get_argument_default_value import get_default_value

def show_options(script):
    option_text = '<div class="col-12 my-2"><div class="card"><div class="card-header">'
    option_text += '<h2 class="text-center">' + script + '</h2>'
    option_text += '''</div>
    <div class="card-body">
        <form action="/perform_attack" method="GET">
        <div class="text-center">
        <h3>Arguments</h3>
    '''
    option_text += '<input type="hidden" name="script" value="' + script + '"'
    option_text += '<div class="col-12 col-lg-6 col-md-6">'
    file = open('GUI/functions/arguments.json','r')
    arguments_in_file = json.load(file)
    for script_args in arguments_in_file[script] :
        args_list = list(script_args.keys())
        for arg in args_list :
            if arg != 'log_name' : # ignore log name in arguments.json
                if (argument_is_required(script_name=script,argument=arg)) :
                    option_text += '<label>' + arg.title() + ' </label>'
                    option_text += '<input class="form-control" type="text" placeholder="Enter ' + arg.title() + '"' + 'name="' + arg + '" required><br><br>'
                else:
                    option_text += '<label>' + arg.title() + ' </label>'
                    option_text += '<input class="form-control" type="text" placeholder="' + get_default_value(script_name=script,argument=arg)[0].title() + '"' + 'name="' + arg + '"><br><br>'

    option_text += '''</div>
            <button class="btn btn-primary btn-block button-attack">Start</button>
            <h3 class="text-center my-4">
                <a href="/show_examples" target="_blank">Show Examples</a>
            </h3>
        </div>
    </form>
    '''

    return option_text

def attack():
    page = render_template('dashboard.html')
    if (request.cookies.get('logged_in') == 'yes'):
        page = page.replace('{to_replace_username}', request.cookies.get('user').title())
    else:
        return redirect('/login', code=302)

    if not (request.args.get('script')) : # if script argument is not set
        return redirect("/scripts", code=302)
        # page = page.replace('{to_replace_text}','<h1 class="text-center">Choose a script ---> <a href="/scripts"> script page</a></h1>')
        # return page
    else:
        chosen_script = request.args.get('script')
        texts = show_options(script=chosen_script)
        page = page.replace('{to_replace_text}' ,texts)
        return page