from flask import Flask, render_template, url_for, flash, redirect, abort, request
from . import main
from .forms import  ComplaintsForm, UpdateProfile 
from app.models import User,Complaints
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

    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


#Tenants list route 

@main.route('/tenants')
@login_required
def tenants(tenants):
    """
    docstring
    """
    tenants = User.query.all()

    return render_template('tenants.html', tenants=tenants)

#adding a complaints
@main.route('/write_complaint/<int:id>', methods=['GET', 'POST'])
@login_required
def complaint(id):
    """ 
    Function to post complaints 
    """
    
    form = ComplaintsForm()
    title = 'post complaint'
    
    if form.validate_on_submit():
        description = form.description.data
        new_complaint = Complaints(description = form.description.data, user_id = current_user.id)
        new_complaint.save_comment()

        flash(f'Your complaint was sent succesfully !', 'success')

        return redirect(url_for('main.index'))

    return render_template('complaint.html', form = form, title = title)


#Updating user profile
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):

    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        user = User(username =form.username.data, room_no= form.room_no.data, email= form.email.data, phone_no= form.phone_no.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
