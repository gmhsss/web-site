from flask import Blueprint, request, render_template, redirect, url_for

login = Blueprint("login",__name__, template_folder="templates")

users = {
"bagriela":"2020",
"anfony":"2002"
}

@login.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('home.html')
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login.html')
    

@login.route('/register_user')
def register_user():
    return render_template("register_user.html")


@login.route('/add_user', methods=['GET','POST'])
def add_users():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        users[user] = password
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
        
    return render_template("users.html", users=users)


@login.route('/list_users')
def list_users():
    global users
    return render_template("users.html", users=users)


@login.route('/remove_user')
def remove_user():
    return render_template("remove_user.html", users=users)


@login.route('/del_user', methods=['GET','POST'])
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        users.pop(user)
    else:
        user = request.args.get('user', None)
        users.pop(user)
    return render_template("users.html", users=users)