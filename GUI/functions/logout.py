#!/usr/bin/env python3

'''
this script is for logout function of the web interface
'''

from flask import make_response,redirect

def logout():
    resp = make_response(redirect('/login',code=302))
    resp.set_cookie('user','',expires=0)
    resp.set_cookie('logged_in','',expires=0)
    return resp