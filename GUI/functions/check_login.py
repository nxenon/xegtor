#!/usr/bin/env python3

'''
this script checks the login information
'''

import json
from flask import redirect,make_response

class CheckLogin:
    def __init__(self,user,user_pass):
        # data user entered
        self.username_in_login = user
        self.password_in_login = user_pass
        # user and password stored in config.json
        self.username_in_app = None
        self.password_in_app = None

    def run(self):
        ret = self.read_login()
        if (ret):
            return ret
        else :
            return self.check_login()

    def read_login(self):
        file = open('GUI/config.json','r')
        data = json.load(file)
        self.username_in_app = data['credentials'][0]['user']
        self.password_in_app = data['credentials'][0]['pass']
        if ((self.username_in_app) and (self.password_in_app)):
            pass
        else:
            return redirect('/login?error=nof') # nof is for no credential found in config.json

    def check_login(self):
        if ((self.username_in_app.lower() == self.username_in_login.lower()) and (self.password_in_app == self.password_in_login)):
            response = make_response(redirect('/dashboard',code=302))
            response.set_cookie('user',self.username_in_app,max_age=3600)
            response.set_cookie('logged_in','yes',max_age=3600)
            return response
        else:
            return redirect('login?error=lf',code=302)