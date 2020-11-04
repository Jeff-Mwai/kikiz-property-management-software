from flask import Flask, render_template, url_for, flash, redirect, abort, request
from . import main
from .forms import RegistrationForm, LoginForm
from ..models import User,ComplaintComment,RentComment,Complaints
from .. import db
from .forms import ComplaintCommentForm,RentCommentForm
from flask_login import login_user,login_required, logout_user, current_user

@main.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    return render_template('index.html')

@main.route('/view_complaint_comments/<id>')
@login_required
def view_complaint_comments(id):
    complaint_comment = ComplaintComment.get_complaint_comments(id)
    title = 'View Complaint Comments'
    return render_template('complaint_comment.html', complaint_comment=complaint_comment,title=title)

@main.route('/complaint_comments/<int:complaint_id>', methods=['GET', 'POST'])
@login_required
def complaint_comment(complaint_id):
    form = ComplaintCommentForm()
    complaint = Complaints.query.filter_by(id=complaint_id).first()
    if form.validate_on_submit():
        complaint_comment = form.complaint_comment.data

        new_complaint_comment = ComplaintComment(complaint_comment=complaint_comment, user_id=current_user.id,complaint_id=complaint_id)
        new_complaint_comment.save_complaint_comment()

        return redirect(url_for('main.tenants'))
    return render_template('complaint_comment.html', form=form, complaint_id=complaint_id)

@main.route('/delete_complaint_comment/<int:complaint_comment_id>', methods=['GET', 'POST'])
@login_required
def delete_complaint_comment(complaint_comment_id):
    complaint_comment =ComplaintComment.query.get(complaint_comment_id)
    if complaint_comment.user.id != current_user.id:
        abort(403)
    db.session.delete(complaint_comment)
    db.session.commit()
   
    return redirect (url_for('main.tenants'))

@main.route('/view_rent_comments/<id>')
@login_required
def view_rent_comments(id):
    rent_comment = RentComment.get_rent_comments(id)
    title = 'View Rent Comments'
    return render_template('rent_comment.html', rent_comment=rent_comment,title=title)

@main.route('/rent_comments/<int:rent_id>', methods=['GET', 'POST'])
@login_required
def rent_comment(complaint_id):
    form = RentCommentForm()
    rent = Rent.query.filter_by(id=rent_id).first()
    if form.validate_on_submit():
        rent_comment = form.rent_comment.data

        new_rent_comment = RentComment(rent_comment=rent_comment, user_id=current_user.id,rent_id=rent_id)
        new_rent_comment.save_rent_comment()

        return redirect(url_for('main.tenants'))
    return render_template('rent_comment.html', form=form, rent_id=rent_id)

@main.route('/delete_rent_comment/<int:rent_comment_id>', methods=['GET', 'POST'])
@login_required
def delete_rent_comment(rent_comment_id):
    rent_comment =RentComment.query.get(rent_comment_id)
    if rent_comment.user.id != current_user.id:
        abort(403)
    db.session.delete(rent_comment)
    db.session.commit()
   
    return redirect (url_for('main.tenants'))

