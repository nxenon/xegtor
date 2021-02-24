#!/usr/bin/env python3

'''
this file is for GUI version of xegtor
'''

from flask import Flask,request,render_template,make_response,redirect,Response
import logging
from threading import Thread
from time import sleep
from modules.get_config_value import get_config_value

# if you start the server for first time cookies will be cleared
reset_number = 1 # 1 is restarted and 0 is not restarted

template_folder_path = 'GUI/templates/'
static_folder_path = 'GUI/static/'
app_main = Flask('__main__',template_folder=template_folder_path,static_folder=static_folder_path)

# disable flask url logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Find the last line of the log file
with open(f'logs/xegtor.log', 'r') as file:
    index_last_log = len(file.readlines())

def logger(log_file_name):
    ''' Read log file'''
    global index_last_log
    while True:
        with open(f'logs/{log_file_name}.log', 'r') as file:
            try:
                yield file.readlines()[index_last_log]
                index_last_log += 1
                sleep(0.2) # delay to show log in template
            except Exception:
                continue

@app_main.route('/')
def index():
    is_reset =  check_reset()
    if (is_reset):
        return is_reset

    from GUI.functions.index import index
    index = index()
    return index

@app_main.route("/stream_log")
def stream_log():
    # log_file_name = request.headers['script'] # Name of the script has been run
    log_file_name = "xegtor"
    return Response(logger(log_file_name), mimetype="text/plain", content_type="text/event-stream") # Build a response to send log

@app_main.route('/login')
def login():
    is_reset = check_reset()
    if (is_reset):
        return is_reset

    from GUI.functions.login import login
    if (request.args.get('error')) :
        login = login(error=request.args.get('error'))
        return login
    else:
        login = login()
        return login

@app_main.route('/check_login',methods=['POST'])
def check_login():
    from GUI.functions.check_login import CheckLogin
    if request.method == 'POST' :
        check = CheckLogin(user=request.form['user'],user_pass=request.form['passw'])
        ret =  check.run()
        return ret

@app_main.route('/dashboard')
def dashboard():
    is_reset = check_reset()
    if (is_reset):
        return is_reset

    from GUI.functions.dashboard import Dashboard
    dashboard = Dashboard().run()
    return dashboard

@app_main.route('/logout')
def logout():
    from GUI.functions.logout import logout
    return logout()

@app_main.route('/forgotpass')
def forgot_password():
    return redirect('https://github.com/xegtor/xegtor/blob/master/docs/forgotpass.md',code=302)

@app_main.route('/scripts')
def scripts():
    is_reset = check_reset()
    if (is_reset):
        return is_reset
    from GUI.functions.scripts import scripts
    scripts = scripts()
    return scripts

@app_main.route('/docs')
def docs():
    is_reset = check_reset()
    if (is_reset):
        return is_reset
    from GUI.functions.docs import docs
    return docs()

@app_main.route('/attack',methods=['GET'])
def attack():
    is_reset = check_reset()
    if (is_reset):
        return is_reset
    from GUI.functions.attack import attack
    attack = attack()
    return attack

@app_main.route('/perform_attack',methods=['GET'])
def perform_attack():
    is_reset = check_reset()
    if (is_reset):
        return is_reset
    from GUI.functions.perform_attack import perform_attack
    perform_attack = perform_attack()
    return perform_attack

@app_main.route('/show_examples')
def show_examples():
    is_reset = check_reset()
    if (is_reset):
        return is_reset
    from GUI.functions.show_examples import show_examples
    show_examples = show_examples()
    return show_examples

@app_main.errorhandler(404)
def page_not_found(e):
    return render_template('404_error.html'), 404

@app_main.errorhandler(500)
def internal_error(e):
    msg = '''
    <h1 style="text-align:center">Internal Server Error (500)</h1>
    <br>
    <h2 style="text-align:center">This might be for bad arguments or bad configuration</h2>
    <br>
    <h2 style="text-align:center">You can restart the script</h2>
    '''
    return msg,500

@app_main.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache' # tell browser not to cache contents
    return response

def check_reset():
    # if server is restarted then the cookies are cleared
    global reset_number
    if (reset_number == 1) :
        reset_number = 0
        if (request.cookies.get('logged_in') or (request.cookies.get('user'))):
            return logout()
    else:
        return ''

def print_url_banner():
    sleep(1)
    flask_url_msg = '\n\tWeb interface running on http://' + str(listening_ip) + ':' + str(port_num) + '/'
    print(flask_url_msg)

port_num = get_config_value(main_key='connection' ,key_in_list='port')
listening_ip = get_config_value(main_key='connection' ,key_in_list='host')

Thread(target=print_url_banner).start() # start a thread to print http url after flask headers

app_main.run(port=port_num ,host=listening_ip)