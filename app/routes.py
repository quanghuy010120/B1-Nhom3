from app import app
from app import form
from app.models import *
from app.form import *
from flask import render_template, request, redirect, flash, url_for, jsonify


@app.route("/")
def index():
    return render_template("index.html", title="Trang chủ")
