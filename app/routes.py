from app import app_inst

@app_inst.route('/')
@app_inst.route('/index')
def index():
    return '''
    <html>
        <head>
            <title>Der Filmmeister Hauptseite</title>
        </head>
        <body>
            Berend, Joris, Jan, Rick
        </body>
    </html>'''