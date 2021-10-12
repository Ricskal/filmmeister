from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app_inst = Flask(__name__)
app_inst.config.from_object(Config)
db = SQLAlchemy(app_inst)
migrate = Migrate(app_inst, db)
login = LoginManager(app_inst)
login.login_view = 'login'

from app import routes, models


# source /Home/filmmeister/venv/bin/activate
# flask run
#alt shift insert