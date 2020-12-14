from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional
import email_validator

class AddSnackForm(FlaskForm):
    """Form for adding snacks."""

    email = StringField('Email', validators=[Email(), Optional()])
    name = StringField('Snack Name', validators=[InputRequired(message='Snack name cannot be blank')])
    price = FloatField('Price in USD')
    quantity = IntegerField('How many?')
    is_healthy = BooleanField('This is a healthy snack')
    
    # category = RadioField('Category', choices=[
    #                         ('ice','Ice Cream'), ('chips', 'Potato Chips'), ('candy', 'Candy')])

    category = SelectField('Category', choices=[
                            ('ice','Ice Cream'), ('chips', 'Potato Chips'), ('candy', 'Candy')])

class EmployeeForm(FlaskForm):
    """Form for adding employees."""

    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    name = StringField('Employee\'s Name', validators=[InputRequired(message='Name cannot be blank')])
    state = SelectField('State', choices=[(state, state) for state in states])
    dept_code = SelectField('Department Code')
