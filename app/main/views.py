from flask import Flask, render_template, url_for, flash, redirect, abort, request
from . import main
from .forms import ComplaintCommentForm,RentCommentForm, UpdateProfile, ComplaintsForm
from ..models import User,ComplaintComment,RentComment,Complaints
from .. import db
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


########################################################################################################################

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

#Tenants list route 
@main.route('/tenants')
@login_required
def tenants():
    """
    docstring
    """
    tenants = User.query.all()

    return render_template('tenants.html', tenants=tenants)


#Adding a complaints
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




    ###################################################################################################################################################################
    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))        
