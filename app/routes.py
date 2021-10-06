from flask import render_template
from app import app_inst
from app.forms import LoginForm


@app_inst.route('/')
@app_inst.route('/index')
def index():
    title = 'Hauptseite'
    body = 'Brend, Joris, Jan, Rick'
    return render_template('index.html', title=title, body=body)


@app_inst.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)
