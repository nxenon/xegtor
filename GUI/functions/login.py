#!/usr/bin/env python3

'''
this script is for login page
'''

from flask import render_template,request,redirect

def login(error=None):
    if (request.cookies.get('logged_in') == 'yes'):
        return redirect('/dashboard',code=302)

    template = render_template('login.html')
    final_page = ''

    # error text for login failure
    error_login_failed = '''
    <br>
    <br>
    <h2 style="color: darkred">Login Failed</h2>
    '''
    error_no_cred_found = '''
    <h2 style="color: darkred">Error : username or password in config.json file did not set</h2>
    '''

    # put error in html if exists
    if (error == 'lf') :
        template = template.replace('{to_replace_error}',error_login_failed) # if login fails it'll print error message in login page
    elif (error == 'nof'):
        template = template.replace('{to_replace_error}',error_no_cred_found) # if there is no user and pass in config.json it will show error
    else:
        template = template.replace('{to_replace_error}','')

    final_page = template
    return final_page