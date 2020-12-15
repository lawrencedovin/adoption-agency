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

class EditPetForm(FlaskForm):
    """Form for editing pets."""
    
    photo_url = StringField('Photo URL', validators=[URL(message='Incorrect URL'), Optional()])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Is pet available?')