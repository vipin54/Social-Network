
# Librarys
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed


from flask_login import current_user
from companyblog.models import User


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Log In')
    
    