from flask import Blueprint, render_template

module = Blueprint("index", __name__, url_prefix="/")


@module.route("/")
def index():
    return render_template('index/index.html')
