#!/usr/bin/env python3

'''
this script is for /scripts page in which you can see scripts
'''

from flask import render_template,request,redirect
from modules.get_scripts_names import get_scripts_names
import re

scripts_names_file_regex = '''(.*):::(.*)'''

def scripts():
    page = render_template('dashboard.html')
    if (request.cookies.get('logged_in') == 'yes'):
        page = page.replace('{to_replace_username}', request.cookies.get('user'))
    else:
        return redirect('/login', code=302)

    script_names = get_scripts_names()
    script_names_desc = re.findall(scripts_names_file_regex,script_names)

    text = '''<br><br><br><br>
    <table>
    <tr>
        <th><h2>Script Name</h2></th>
        <th><h2>Description</h2></th>
        <th><pre>   </pre><h2>Link</h2><pre>   </pre></th>
    </tr>
    <br>
    '''
    for s in script_names_desc :
        text += '<tr><td><pre>    <b><h3>' + s[0] + '</h3></b>    </pre></td><td><pre>    <h3>' + s[1] + '</h3>    </pre></td><td>' + '<pre>    <a href="/attack?script=' + s[0] + '"><h3>use script</h3></a>    </pre></td></tr>'

    text += '</table>'
    final_page = page.replace('{to_replace_text}',text)
    return final_page