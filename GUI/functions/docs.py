#!/usr/bin/env python3

'''
this script is for /examples page in which you can see scripts examples
'''

from flask import redirect

def docs():
    return redirect('https://github.com/xenon-xenon/xegtor/blob/master/scripts/README.md',code=302)