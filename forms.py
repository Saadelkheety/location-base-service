from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators

class SignupForm(FlaskForm):
    first_name = StringField('First name', [validators.DataRequired("please enter you first name")])
    last_name = StringField('Last name', [validators.DataRequired('please enter you last name')])
    email = StringField('Email', [validators.DataRequired('please enter your email'), validators.Email('please enter your real email address')])
    password = PasswordField('Password', [validators.DataRequired('please enter a password'), validators.Length(min=6, message="Passwords must be 6 characters or more.")])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
  email = StringField('Email', [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your real email address.")])
  password = PasswordField('Password', [validators.DataRequired("Please enter a password.")])
  submit = SubmitField("Sign in")

class AddressForm(FlaskForm):
    address = StringField('Adress', [validators.DataRequired("please enter the address")])
    submit = SubmitField('Search')
