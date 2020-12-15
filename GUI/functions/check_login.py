#!/usr/bin/env python3

'''
this script checks the login information
'''

from flask import redirect,make_response
from modules.get_config_value import get_config_value

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
        self.username_in_app = get_config_value(main_key='credentials' ,key_in_list='user')
        self.password_in_app = get_config_value(main_key='credentials' ,key_in_list='pass')
        if ((self.username_in_app) and (self.password_in_app)):
            pass
        else:
            print('[!] web login failed')
            return redirect('/login?error=nof') # nof is for no credential found in config.json

    def check_login(self):
        if ((self.username_in_app.lower() == self.username_in_login.lower()) and (self.password_in_app == self.password_in_login)):
            print('[+] web login succeeded')
            response = make_response(redirect('/dashboard',code=302))
            response.set_cookie('user',self.username_in_app,max_age=3600)
            response.set_cookie('logged_in','yes',max_age=3600)
            return response
        else:
            print('[!] web login failed')
            return redirect('login?error=lf',code=302)