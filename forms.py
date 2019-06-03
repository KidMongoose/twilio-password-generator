from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import NumberRange, DataRequired
from wtforms.fields.html5 import TelField, IntegerField


class PasswordForm(FlaskForm):
    telephone_number_field = TelField(validators=[DataRequired()])
    password_length_field = IntegerField(validators=[DataRequired()])
    send = SubmitField('Get password')


