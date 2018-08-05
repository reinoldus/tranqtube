from pprint import pprint

from flask import render_template, jsonify, request
from pymongo import MongoClient
import base64
from tranqtube import app

# this should be fine
client = MongoClient(app.config['MONGO'])
db = client.tranqtube


@app.route('/')
def index():
    videos = db['videos']
    videos = videos.find()

    app.logger.warning('sample message')
    return render_template('index.html', videos=videos, base64=base64)


@app.route('/play/<web_path>')
def play(web_path):
    videos = db['videos']
    video = videos.find_one({"full_web_path": base64.b64decode(web_path).decode()})

    return render_template('play.html', video=video)


@app.route('/pause', methods = ['GET', 'POST'])
def pause():
    data = request.json
    videos = db['videos']
    video = videos.find_one_and_update(
        {"full_web_path": data['src']},
        {'$set': {'paused': data['time']}}
    )
    return jsonify(data)


@app.route('/leaving', methods = ['GET', 'POST'])
def leaving():
    data = request.json
    videos = db['videos']
    video = videos.find_one_and_update(
        {"full_web_path": data['src']},
        {'$set': {'last_left': data['time']}}
    )
    print("??")

    return jsonify(data)
