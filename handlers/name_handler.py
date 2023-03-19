from flask import render_template
import os

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, 'pages/')


def name_handler(name):
    return render_template("./pages/home.html")
# This file hasn't been used yet
