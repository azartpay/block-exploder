from flask import Flask, render_template
from flask_socketio import SocketIO, emit, disconnect
import gevent

BLOCK_TX_THREAD_SLEEP = 3
PRICE_STATS_THREAD_SLEEP = 240

ASYNC_MODE = 'gevent'

LATEST_FIVE_BLOCKS_URL = 'http://127.0.0.1:5001/api/blocks/latest?limit=5'
LATEST_N_TX_URL = 'http://127.0.0.1:5001/api/transactions/latest?limit='
LATEST_PRICE_STATS_URL = 'http://127.0.0.1:5001/api/network/price-stats'

app = Flask(__name__)
socketio = SocketIO(app, async_mode=ASYNC_MODE, ping_timeout=4000)
