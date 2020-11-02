#!/usr/bin/env python3

'''
script for return main page index
'''

from flask import redirect

def index():
    return redirect('/login',code=302)