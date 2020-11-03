#!/usr/bin/env python3

'''
this script is for /attack page in which you can start attacks
'''

from flask import render_template,request,redirect

def attack():
    page = render_template('dashboard.html')
    if (request.cookies.get('logged_in') == 'yes'):
        page = page.replace('{to_replace_username}', request.cookies.get('user'))
    else:
        return redirect('/login', code=302)
    return 'test'