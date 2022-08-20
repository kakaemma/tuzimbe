from crypt import methods
from flask import render_template, request
from app import create_app
from classes.worker import Worker
from utility.request_utility import validate_content_type

app = create_app('DevelopmentEnv')

@app.route('/')
def index():
    """
    index route
    """
    return render_template('index.html')

@app.route('/api/<version>/register', methods=['POST'])
@validate_content_type
def registe_user(version):
    request.get_json(force=True)
    name = request.json['name']
    user_type = request.json['user_type']
    response = Worker.register_worker(name, user_type)
    return response

@app.route('/api/<version>/work/daily', methods=['POST'])
@validate_content_type
def capture_work_details(version):
    request.get_json(force=True)
    user_id = request.json['user_id']
    arrival_time = request.json['arrival_time']
    departure_time = request.json['departure_time']
    daily_rate = request.json['daily_rate']
    response = Worker.capture_wrk_details(
        user_id, daily_rate, arrival_time,departure_time)
    return response
