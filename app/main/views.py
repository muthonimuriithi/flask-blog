from flask import render_template
from app.main import main

@main.route('/')
def index ():
    heading="hopefully ours"
    return render_template('index.html', heading=heading)
