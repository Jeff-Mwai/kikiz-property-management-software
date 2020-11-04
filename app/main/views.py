from flask import Flask, render_template, url_for, flash, redirect, abort, request
from . import main
from .forms import  ComplaintsForm, RegistrationForm, LoginForm, 
from app.models import User,Complaints
, Comments, Votes
from ..models import User
from .. import db
from flask_login import login_user,login_required, logout_user, current_user


@main.route('/')
def home():
    return render_template('index.html')



#user profile route

@main.route('/user/<uname>')
@login_required
def profile(uname):

    img_file =url_for('static', filename='current_user.')
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/tenants')
@login_required
def tenants(tenants):
    """
    docstring
    """
    tenants = User.query.all()

    return render_template('tenants.html', tenants=tenants)



#adding a comment
@main.route('/write_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def post_comment(id):
    """ 
    Function to post comments 
    """
    
    form = ComplaintsForm()
    title = 'post comment'
    
    if form.validate_on_submit():
        description = form.description.data
        new_complaint = Complaints(description = form.description.data, user_id = current_user.id, pitches_id = pitches.id)
        new_complaint.save_comment()
        return redirect(url_for('main.view_pitch', id = pitches.id))

    return render_template('comments.html', form = form, title = title)
