from gevent.wsgi import WSGIServer
from flask7 import app

http_server = WSGIServer(('127.0.0.1', 5000), app)
http_server.serve_forever()