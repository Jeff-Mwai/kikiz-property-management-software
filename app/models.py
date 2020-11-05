from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader

def load_user(user_id):
    return User.query.get(int(user_id))
    


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    phone_no = db.Column(db.String(20),unique = True, index = True)
    id_no = db.Column(db.Integer,unique = True, index = True)
    role = db.Column(db.String(255),index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

class Complaints(db.Model):
    __tablename__ = 'complaints'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    description = db.Column(db.String(255))
    resolution = db.Column(db.String(255))
    complaint_sorted = db.Column(db.String(255))
    dated = db.Column(db.Date)

class Rent(UserMixin,db.Model):
    __tablename__ = 'rent'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    amount = db.Column(db.Numeric(10,2))
    description = db.Column(db.String(255))
    month = db.Column(db.String(255))
    dated = db.Column(db.Date)

class  ComplaintComment(db.Model):
    __tablename__='complaint_comment'

    id = db.Column(db.Integer, primary_key=True)
    complaint_comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    complaint_id = db.Column(db.Integer, db.ForeignKey("complaints.id"))

    def save_complaint_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_complaint_comments(cls,id):
        comments = Comment.query.filter_by(complaint_id=id).all()
        return comments

    def __repr__(self):
        return f'Complaint Comment: {self.complaint_comment}'

class RentComment(db.Model):
    __tablename__='rent_comment'

    id = db.Column(db.Integer, primary_key=True)
    rent_comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    rent_id = db.Column(db.Integer, db.ForeignKey("rent.id"))

    def save_rent_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_rent_comments(cls,id):
        comments = Comment.query.filter_by(rent_id=id).all()
        return comments

    def delete_rent_comment(self):
        db.session.delete(self)
        db.session.commit()    

    def __repr__(self):
        return f'The Rent Comment: {self.rent_comment}'

