from flask import render_template, flash, redirect, url_for
from app import app_inst
from app.forms import LoginForm



@app_inst.route('/')
@app_inst.route('/index')
def index():
    title = 'Hauptseite'
    body = 'Berend, Joris, Jan, Rick'
    return render_template('index.html', title=title, body=body)


@app_inst.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {} remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)
