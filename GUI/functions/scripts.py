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
        page = page.replace('{to_replace_username}', request.cookies.get('user').title())
    else:
        return redirect('/login', code=302)

    script_names = get_scripts_names()
    script_names_desc = re.findall(scripts_names_file_regex,script_names)

    text = '''<br><br><br><br><div class="script_table" style="text-align : center">
    <table class="center">
    <tr>
        <th><h2><pre>       Link      </pre></h2></th>
        <th><h2><pre>   Description   </pre></h2></th>
        <th><h2><pre>   Script Name   </pre></h2></th>
    </tr>
    <br>
    '''
    for s in script_names_desc :
        text += '<tr><td>' + '<pre>    <a href="/attack?script=' + s[0] + '"><h3>use script</h3></a>    </pre></td><td><pre>    <h3>' + s[1] + '</h3>     </pre></td>' + '<td><pre>    <b><h3>' + s[0] + '</h3></b></tr>'

    text += '</table></div>'
    final_page = page.replace('{to_replace_text}',text)
    return final_page