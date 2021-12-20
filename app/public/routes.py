from flask import render_template, redirect, url_for

from . import public_bp

@public_bp.route("/")
def index():
    return render_template("public/index.html", data="INDEX")
