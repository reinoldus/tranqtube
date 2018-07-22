from flask import render_template, jsonify

from tranqtube import app


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')


@app.route('/pause/<pause_time>')
def pause(pause_time):
    app.logger.warning('sample message', pause_time)

    return jsonify({
        "time": pause_time
    })
