from flask import render_template
from api import create_app

app = create_app('DevelopmentEnv')

@app.route('/')
def index():
    """
    index route
    """
    return render_template('index.html')



