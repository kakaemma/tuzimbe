from crypt import methods
from flask import render_template, request
from app import create_app
from classes.worker import Worker
from  utility.class_utility import invalid_keys
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
