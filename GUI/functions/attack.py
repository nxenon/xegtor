#!/usr/bin/env python3

'''
this script is for /attack page in which you can start attacks
'''

from flask import render_template,request,redirect
import json

def show_options(script):
    option_text = '<br><br><h2 style="text-align : center">' + script + '</h2><br><br>'
    option_text += '''
    <form action="/perform_attack" method="get">
    <div style="text-align : center">
    <h2>Arguments</h2><br>
    '''
    option_text += '<input type="hidden" name="script" value="' + script + '"'

    file = open('GUI/functions/arguments.json','r')
    arguments = json.load(file)
    for args in arguments[script] :
        args_list = list(args.keys())
        for a in args_list :
            if (args[a] == '*') : # if the argument is required
                option_text += '<label>' + a.title() + ' </label>'
                option_text += '<input style="font-size : 25px" type="text" placeholder="Enter ' + a.title() + '"' + 'name="' + a + '" required><br>'
            else:
                option_text += '<label>' + a.title() + ' </label>'
                option_text += '<input style="font-size : 25px" type="text" placeholder="' + args[a].title() + '"' + 'name="' + a + '"><br>'

    option_text += '''
    <button style="font-size: 20px" type="submit">start</button>
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
        page = page.replace('{to_replace_text}','<h1 style="text-align : center">Choose a script ---> <a href="/scripts"> script page</a></h1>')
        return page
    else:
        chosen_script = request.args.get('script')
        texts = show_options(script=chosen_script)
        page = page.replace('{to_replace_text}',texts)
        return page