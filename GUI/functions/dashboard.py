#!/usr/bin/env python3

'''
this script is for dashboard page of the web interface
'''

from flask import render_template,request,redirect

class Dashboard():
    def __init__(self):
        pass

    def run(self):
        if (request.cookies.get('logged_in') == 'yes') :
            page = self.read_page()
            page = page.replace('{to_replace_username}',request.cookies.get('user').capitalize())
            page = page.replace('{to_replace_text}','')
            return page
        else:
            return redirect('/login',code=302)

    def check_auth(self):
        pass

    def read_page(self):
        template = render_template('dashboard.html')
        return template