# from gevent import monkey
# monkey.patch_all()

from app import socketio, app


socketio.run(app,host ='0.0.0.0',port=443,keyfile='server.key', certfile='server.crt')