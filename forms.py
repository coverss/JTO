from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,FileField,TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from datetime import date

class PostForm(FlaskForm):
    text = TextAreaField('text', validators=[DataRequired()],render_kw={'rows':'4'})
    submit = SubmitField('Submit',render_kw={'class': 'ui small green button'})
    #upload = SubmitField('Upload and Submit',render_kw={'class': 'ui small green button'})
    postimage = FileField('upload image')

class UploadUserImageForm(FlaskForm):

    userimage = FileField('Image file',validators=[DataRequired()])
    upload = SubmitField('Upload')

class RelationForm(FlaskForm):

    addfriend = SubmitField('Add Friend')

#DataRequired - it cannot be empty
class RegistrationForm(FlaskForm):
    name = StringField('name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    'checks whether the database already has this name'
    def validate_name(self,name):
        user = User.query.filter_by(name = name.data).first()
        if user:
            raise ValidationError('That username is taken.')
            
    'checks whether the database already has this email'
    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('That email is taken.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    

class UpdateAccountForm(FlaskForm):
    name = StringField('name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('password',
                        validators=[DataRequired()])
    weight = StringField('weight',
                        validators=[DataRequired()])
    city = StringField('city',
                        validators=[DataRequired()])
    interest = StringField('interest',
                        validators=[DataRequired()])
    languages = StringField('languages',
                        validators=[DataRequired()])
    birthday = DateField('Start Date',default=date.today(), format='%m/%d/%Y')
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])]) # I didnt use it
    submit = SubmitField('Update')





   

    
  
 