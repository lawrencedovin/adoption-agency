""""Seed file to make sample data for db."""

from models import *
from app import app

# Create all tables
db.drop_all()
db.create_all()

jerry = Pet(name="Jerry",
            species="Dog", 
            photo_url="https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1949&q=80",
            age = 10)

samantha = Pet(name="Samantha", 
            species="Bird", 
            photo_url="https://images.unsplash.com/photo-1551085254-e96b210db58a?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1486&q=80",
            age = 12)

ricardo = Pet(name="Ricardo", 
            species="Dog",
            photo_url="https://images.unsplash.com/photo-1546447147-3fc2b8181a74?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=934&q=80",
            age = 6)

rock = Pet(name="Rock", 
            species="Lizard",
            photo_url="https://images.unsplash.com/photo-1504450874802-0ba2bcd9b5ae?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80",
            age = 3,
            available = False)

db.session.add_all([jerry, samantha, ricardo, rock])

db.session.commit()