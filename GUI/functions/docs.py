#!/usr/bin/env python3

'''
this script is for /docs page in which you can see scripts README
'''

from flask import redirect

def docs():
    return redirect('https://github.com/xegtor/xegtor/blob/master/scripts/README.md',code=302)