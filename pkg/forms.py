from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,PasswordField,EmailField,SelectField,
                     TextAreaField,BooleanField)
from wtforms.validators import DataRequired,Length,Email,EqualTo


class UserDetail(FlaskForm):
    surname = StringField('Surname',validators=[DataRequired(message='You did not type a surname'),Length(min=3,max=5,message='Surname must not be above 5 characters')])
    firstname = StringField('Firstname',validators=[DataRequired(message='Firstname field is important')])
    email = EmailField('Email',validators=[DataRequired(),Email(message='The email you entered is invalid')])
    password = PasswordField('Password',validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password',message='Passwords does not match')])
    bio = TextAreaField('Bio')
    agree = BooleanField('Do you agree with our TC ?',validators=[DataRequired()])
    submit = SubmitField('Submit')


class SignUpForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = EmailField('Email Address',validators=[DataRequired(),Email()])
    password1 = PasswordField('Password',validators=[DataRequired()])
    password2 = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password1')])
    gender = SelectField('Gender',choices=[('m','Male'),('f','Female')])
    signup = SubmitField('Sign Up')

    class Meta:
        csrf=True
        csrf_time_limit=7200
