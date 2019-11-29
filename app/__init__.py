import os
from flask import Flask
import datetime
from flask_socketio import SocketIO

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False
app.config["MONGODB_HOST"] = "mongodb+srv://kang:kkkk0000@cluster0-ew3ql.gcp.mongodb.net/test?retryWrites=true&w=majority" #os.environ.get('HOSTDB_ADDR') 
app.config["MONGODB_DB"] = True
app.config['SECRET_KEY'] = 'ntouMOTOgo' #os.environ.get('SECRET_KEY')
app.config['BCRYPT_LOG_ROUNDS'] = 10
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.permanent_session_lifetime = datetime.timedelta(days=1) #登入時效
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

socketio = SocketIO(app, async_mode='threading')

from .main import backend, _socket, _login