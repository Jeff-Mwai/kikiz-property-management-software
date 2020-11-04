from wtforms.validators import Required, Email, EqualTo
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField, TextAreaField, SelectField, validators 
from flask_wtf import FlaskForm



class ComplaintsForm(FlaskForm):

    description = TextAreaField('Leave a comment/complaints:',validators=[Required()])
    submit = SubmitField('Submit')
