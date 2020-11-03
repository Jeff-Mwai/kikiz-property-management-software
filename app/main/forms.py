from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import Required

class ComplaintComment(FlaskForm):
    complaint_comment = TextAreaField('Leave a Comment', validators=[Required()])
    submit = SubmitField('Submit')

class RentComment(FlaskForm):
    rent_comment = TextAreaField('Leave a Comment', validators=[Required()])
    submit = SubmitField('Submit')