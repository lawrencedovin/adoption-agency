from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# MODELS GO BELOW!

class Department(db.Model):
    """Department Model"""

    __tablename__ = 'departments'

    dept_code = db.Column(db.Text, primary_key=True)
    dept_name = db.Column(db.Text, nullable=False, unique=True)
    phone = db.Column(db.Text)

    def __repr__(self):
        return f'<Department {self.dept_code} {self.dept_name} {self.phone}>'
        
    # employees = db.relationship('Employee')

class Employee(db.Model):
    """Employee Model"""

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    state = db.Column(db.String(2), nullable=False, default='CA')
    dept_code = db.Column(db.Text, db.ForeignKey('departments.dept_code'))    
    
    # department = db.relationship('Department')
    department = db.relationship('Department', backref='employees')

    assignments = db.relationship('EmployeeProject', backref='employee')

    projects = db.relationship('Project', secondary='employees_projects', backref='employees')
    
    def __repr__(self):
        return f'<Employee {self.name} {self.state} {self.dept_code}>'

class Project(db.Model):
    """Project Model"""

    __tablename__ = 'projects'

    proj_code = db.Column(db.Text, primary_key=True)
    proj_name = db.Column(db.Text, nullable=False, unique=True)

    assignments = db.relationship('EmployeeProject', backref='project')

class EmployeeProject(db.Model):
    """Employee Project Model"""

    __tablename__ = 'employees_projects'

    emp_id = db.Column(db.Integer, db.ForeignKey('employees.id'), primary_key=True)
    proj_code = db.Column(db.Text, db.ForeignKey('projects.proj_code'), primary_key=True)
    role = db.Column(db.Text)

def get_directory():
    employees = Employee.query.all()

    for employee in employees:
        if employee.department is not None:
            print(employee.name, employee.department.dept_name, employee.department.phone)  
        else:
            print(employee.name, '-', '-')

def get_directory_join():
    directory = db.session.query(
        Employee.name, Department.dept_name, Department.phone).join(Department).all()
    
    for name, department, phone in directory:
        print(name, department, phone)

def get_directory_join_2():
    directory = db.session.query(Employee, Department).join(Department).all()
    
    for emp, dept in directory:
        print(emp.name, dept.dept_name, dept.phone)

def get_directory_outerjoin_left():
    """Gets all of the Employee data and gets Department data if matched"""

    directory = db.session.query(Employee, Department).outerjoin(Department).all()
    
    for emp, dept in directory:
        if dept:
            print(emp.name, dept.dept_name, dept.phone)
        else:
            print(emp.name, '-', '-')

def get_directory_outerjoin_right():
    """Gets all of the Department data and gets Employee data if matched"""

    directory = db.session.query(Employee, Department).outerjoin(Employee).all()
    
    for emp, dept in directory:
        if emp:
            print(emp.name, dept.dept_name, dept.phone)
        else:
            print('-', dept.dept_name, dept.phone)