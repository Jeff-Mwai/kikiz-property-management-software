from flask import Flask, render_template, url_for, flash, redirect, abort, request
from . import main
from .forms import RegistrationForm, LoginForm
from ..models import User,ComplaintComment,RentComment,Complaints
from .. import db
from .forms import ComplaintCommentForm,RentCommentForm
from flask_login import login_user,login_required, logout_user, current_user

@main.route('/')
def home():
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
