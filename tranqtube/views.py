from flask import render_template, jsonify
from pymongo import MongoClient
import base64
from tranqtube import app


@app.route('/')
def index():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.tranqtube
    videos = db['videos']
    videos = videos.find()

    app.logger.warning('sample message')
    return render_template('index.html', videos=videos, base64=base64)


@app.route('/play/<web_path>')
def play(web_path):

    web_path = base64.b64decode(web_path).decode()

    return render_template('play.html', web_path=web_path)


@app.route('/pause/<pause_time>')
def pause(pause_time):
    app.logger.warning('sample message', pause_time)

    return jsonify({
        "time": pause_time
    })
