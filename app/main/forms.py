
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField, TextAreaField, validators, IntegerField 
from wtforms.validators import Required, Email

class ComplaintCommentForm(FlaskForm):
    complaint_comment = TextAreaField('Leave a Comment', validators=[Required()])
    submit = SubmitField('Submit')

class RentCommentForm(FlaskForm):
    rent_comment = TextAreaField('Leave a Comment', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class ComplaintsForm(FlaskForm):

    description = TextAreaField('Leave a comment/complaints:',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    username = StringField('username', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    room_no = StringField('House No', validators=[Required()])
    phone_no = IntegerField('Phone Number', validators=[Required()])
    submit = SubmitField('UPDATE')
