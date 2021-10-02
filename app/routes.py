from app import app_ints

@app_ints.route('/')
@app_ints.route('/index')
def index():
    return "Berend Joris Jan Rick"