from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import Required

class ComplaintCommentForm(FlaskForm):
    complaint_comment = TextAreaField('Leave a Comment', validators=[Required()])
    submit = SubmitField('Submit')

class RentCommentForm(FlaskForm):
    rent_comment = TextAreaField('Leave a Comment', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

