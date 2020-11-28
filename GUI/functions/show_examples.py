#!/usr/bin/env python3

'''
this script is for /show_examples page in which you can see scripts examples
'''

from flask import redirect

def show_examples():
    return redirect('https://github.com/xegtor/xegtor/blob/master/scripts/examples.txt',code=302)