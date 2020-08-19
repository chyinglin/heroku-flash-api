from flask import Flask, request, render_template, redirect, url_for
from flask import flash

app = Flask(__name__)
app.secret_key = "febe"

# 01: route index
@app.route('/')
def index():
    return "hello"

# 02: pass value
@app.route('/user/<username>')
def username(username):
    return 'i am ' + username

@app.route('/age/<int:age>')
def userage(age):
    return 'i am ' + str(age) + ' years old'

# 03: url_for
@app.route('/a')
def url_for_a():
    return 'here is a'

@app.route('/b')
def b():
    #  會將使用者引導到'/a'這個路由
    #  url_for('url_for_a') 所得結果為'/a'
    return redirect(url_for('url_for_a'))

# 04: type error to trigger app.debug = True
@app.route('/error')
def error_type():
    is_int = 3
    return 'display string ' + is_int

# 05+06: render template and pass value
@app.route('/para/<user>')
def index_user(user):
    return render_template('abc.html', user_template=user)

# 07: send request
# @app.route('/login', methods=['GET', 'POST']) 
# def login():
#     if request.method == 'POST': 
#         return 'Hello ' + request.values['username'] 
#     return "<form method='post' action='/login'><input type='text' name='username' />" \
#             "</br>" \
#            "<button type='submit'>Submit</button></form>"
# 08: change action='/login' to use url_for is better
# @app.route('/loginurl', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return 'Hello ' + request.values['username']
#     return render_template('login.html')

# 09: pass value from form to html
# @app.route('/loginurl', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return redirect(url_for('hello', username=request.form.get('username')))

#     return render_template('login.html')

# @app.route('/hello/<username>')
# def hello(username):
#     return render_template('hello.html', username=username)


# # 10:
# @app.route('/loginurl', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         if login_check(request.form['username'], request.form['password']):
#             flash('Login Success!')
#             return redirect(url_for('hello', username=request.form.get('username')))
#     return render_template('login.html')

# def login_check(username, password):
#     """登入帳號密碼檢核"""
#     if username == 'admin' and password == 'hello':
#         return True
#     else:
#         return False

# @app.route('/hello/<username>')
# def hello(username):
#     return render_template('hello.html', username=username)

# 11: jinja2
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if login_check(request.form['username'], request.form['password']):
            flash('Login Success!')
        return redirect(url_for('hello', username=request.form.get('username')))

    return render_template('login.html')

def login_check(username, password):
    """登入帳號密碼檢核"""
    if username == 'admin' and password == 'hello':
        return True
    else:
        return False

@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)


if __name__ == '__main__':
    app.debug = True
    app.run()
