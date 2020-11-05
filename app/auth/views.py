from flask import render_template
from . import auth
from ..models import User
from .. import db
from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user,logout_user,login_required, current_user
from .forms import LoginForm,RegistrationForm, AdminForm
from ..email import mail_message

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.tenants',uname=current_user.username))
      
        flash('Invalid username or Password')

    title = "Login"
    return render_template('auth/login.html',login_form = login_form,title=title)


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data ,password = form.password.data, phone_no = form.phone_no.data, id_no = form.id_no.data, house_no = form.house_no.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to Kikiz Property Management","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form = form)


@auth.route('/admin',methods=['GET','POST'])
def create_admin():
    admin_form = AdminForm()
    if request.method == "POST":
        new_user = User(username = request.form['username'], email = request.form['email'], password = request.form['password'], is_admin=True)
        db.session.add(new_user)
        db.session.commit()
        return "you have created an admin account"
    title = "login"
    return render_template('auth/admin.html',admin_form = admin_form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))    