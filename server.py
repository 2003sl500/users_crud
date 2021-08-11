from flask import Flask, render_template, request, redirect
from users import Users

app = Flask(__name__)

@app.route('/')
def index():

    users_info = Users.get_all()
    print(users_info)
    
    return render_template('read.html', all_users = users_info)

@app.route('/users')
def users():

    return render_template('create.html')

@app.route('/add_user', methods = ['POST'])
def add_user():

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }

    Users.save(data)

    return redirect('/')

@app.route('/show_user/<int:id>')
def show_user(id):
    print("User Id: ", id)
    users_info = Users.single_user(id)

    return render_template('show_user.html', all_users = users_info)

@app.route('/edit_user/<int:id>')
def edit_user(id):
    print("edit user pressed ", id)
    users_info = Users.edit(id)
    print(users_info)

    return render_template('/edit.html', id = id, all_users = users_info)

@app.route('/edit', methods = ['POST'])
def edit():

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }

    Users.edit(data)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)