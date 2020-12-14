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
            species="Dog")

db.session.add_all([jerry, samantha, ricardo])

db.session.commit()

# marketing = Department(dept_code='mktg', dept_name='Marketing', phone='610-2999')
# accounting = Department(dept_code='acct', dept_name='Account', phone='610-2932')
# sales = Department(dept_code='sales', dept_name='Sales')

# billy = Employee(name='Billy Joel', state='MD', dept_code='mktg')
# buko = Employee(name='Buko Pie', state='NY', dept_code='mktg')
# bob = Employee(name='Bob Ross', state='PA', dept_code='acct')
# jim = Employee(name='Jim Halpert', state='PA', dept_code='sales')
# ryan = Employee(name='Ryan Reynalds', dept_code='sales')
# freelancer = Employee(name='Free Lancer')

# car = Project(proj_code='car', proj_name='Design Car')
# server = Project(proj_code='server', proj_name='Deploy Server')

# billy_job_1 = EmployeeProject(emp_id=1, proj_code='car', role='Blueprints Car')
# billy_job_2 = EmployeeProject(emp_id=1, proj_code='server', role='Serves Ice Cream')
# buko_job = EmployeeProject(emp_id=2, proj_code='server', role='Serves Pizza')

# db.session.add_all([marketing, accounting, sales])
# db.session.add_all([billy, buko, bob, jim, ryan, freelancer])
# db.session.add_all([car, server])
# db.session.commit()

# db.session.add_all([billy_job_1, billy_job_2, buko_job])
# db.session.commit()