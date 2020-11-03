from flask import Flask, render_template, url_for, flash, redirect, abort, request
from . import main
from ..models import User
from .. import db
from flask_login import login_user,login_required, logout_user, current_user

@main.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    return render_template('index.html')