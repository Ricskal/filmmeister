from flask import render_template
from app import app_inst

@app_inst.route('/')
@app_inst.route('/index')
def index():
    title = 'Hauptseite'
    body = 'Brend, Joris, Jan, Rick'
    return render_template('index.html', title = title, body = body)