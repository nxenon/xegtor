#!/usr/bin/env python3

'''
this file is for GUI version of xegtor
'''

from flask import Flask,request,render_template,make_response,redirect

# if you start the server for first time cookies will be cleared
reset_number = 1 # 1 is restarted and 0 is not restarted

template_folder_path = 'GUI/templates/'
static_folder_path = 'GUI/static/'
app_main = Flask('__main__',template_folder=template_folder_path,static_folder=static_folder_path)

@app_main.route('/')
def index():
    is_reset =  check_reset()
    if (is_reset):
        return is_reset

    from GUI.functions.index import index
    index = index()
    return index

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

@app_main.errorhandler(404)
def page_not_found(e):
    return render_template('404_error.html'), 404

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

app_main.run(port=8484)