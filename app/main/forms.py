from wtforms.validators import Required, Email, 
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField, TextAreaField, validators, IntegerField 
from flask_wtf import FlaskForm



class ComplaintsForm(FlaskForm):

    description = TextAreaField('Leave a comment/complaints:',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    username = StringField('username', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    room_no = StringField('House No', validators=[Required()])
    phone_no = IntegerField('Phone Number', validators=[Required()])
    submit = SubmitField('UPDATE')
