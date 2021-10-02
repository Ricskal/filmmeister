from app import app_inst

@app_inst.route('/')
@app_inst.route('/index')
def index():
    return "Berend Joris Jan Rick"