import time
import socket
import redis
from flask import Flask
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
def get_hit_count():
	return cache.incr('hits')

@app.route('/')
def hello():
	count = get_hit_count()
	return 'Hello VERSION 3.11.0! You are mine {} viewer. My name is: {}\n'.format(count, socket.gethostname())
