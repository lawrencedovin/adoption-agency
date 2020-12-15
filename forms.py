from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    species = ['dog', 'cat', 'porcupine', 'lizard', 'bird']

    name = StringField('Pet name', validators=[InputRequired(message='Pet name cannot be blank')])
    species = SelectField('Species', choices=[(species, species.capitalize()) for species in species])
    photo_url = StringField('Photo URL', validators=[URL(message='Incorrect URL'), Optional()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30, message='Must be between ages 0 to 30'), Optional()])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Is pet available?')

# class AddSnackForm(FlaskForm):
#     """Form for adding snacks."""

#     email = StringField('Email', validators=[Email(), Optional()])
#     name = StringField('Snack Name', validators=[InputRequired(message='Snack name cannot be blank')])
#     price = FloatField('Price in USD')
#     quantity = IntegerField('How many?')
#     is_healthy = BooleanField('This is a healthy snack')
    
    # category = RadioField('Category', choices=[
    #                         ('ice','Ice Cream'), ('chips', 'Potato Chips'), ('candy', 'Candy')])

    # category = SelectField('Category', choices=[
    #                         ('ice','Ice Cream'), ('chips', 'Potato Chips'), ('candy', 'Candy')])

# class EmployeeForm(FlaskForm):
#     """Form for adding employees."""

#     states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
#           "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
#           "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
#           "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
#           "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#     name = StringField('Employee\'s Name', validators=[InputRequired(message='Name cannot be blank')])
#     state = SelectField('State', choices=[(state, state) for state in states])
#     dept_code = SelectField('Department Code')

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # name = db.Column(db.Text, nullable=False)
    # species = db.Column(db.Text, nullable=False)
    # photo_url = db.Column(db.Text)
    # age = db.Column(db.Integer)
    # notes = db.Column(db.Text)
    # available = db.Column(db.Boolean, nullable=False, default=True)