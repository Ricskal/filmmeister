from flask import Flask

app_inst = Flask(__name__)

from app import routes

# /Home/filmmeister/venv/bin/activate
# flask run