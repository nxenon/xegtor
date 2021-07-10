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

    text = '''
    <div class="col-12">
        <div class="card">
            <div class="card-header">
                <h4 class="card-title">Scripts</h4>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-striped table-responsive">
                        <thead>
                            <tr>
                                <th>Link</th>   
                                <th>Description</th>
                                <th>Script Name</th>
                            </tr>
                        </thead>
                        <tbody>
    '''
    for s in script_names_desc :
        text += '<tr><td>' + '<a class="btn btn-success light sharp" href="/attack?script=' + s[0] + '"><i class="flaticon-381-link"></i></a></td><td>' + s[1] + '</td>' + '<td>' + s[0] + '</tr>'

    text += '</tbody></table></div>'
    final_page = page.replace('{to_replace_text}',text)
    return final_page