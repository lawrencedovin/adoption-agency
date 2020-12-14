from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import *
from forms import AddSnackForm, EmployeeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'chickenzarecool123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/phones')
def list_phones():
    employees = Employee.query.all()
    return render_template('phones.html', employees=employees)

@app.route('/snacks/new', methods=['GET', 'POST'])
def add_snack():
    """Snack add form; handle adding."""

    form = AddSnackForm()

    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        quantity = form.quantity.data
        total_price = price * quantity
        is_healthy = form.is_healthy.data
        if is_healthy:
            flash(f'Added {name} at ${price} each and a healthy snack. Quantity: {quantity}, total price: ${total_price}')
        else: 
            flash(f'Added {name} at ${price} and a junkfood snack. Quantity: {quantity}, total price: ${total_price}')
        return redirect('/')
    else:
        return render_template('add_snack_form.html', form=form)

@app.route('/employees/new', methods=['GET', 'POST'])
def add_employee():

    form = EmployeeForm()

    # Adds a tuple to the dept_code.choices select form field ie. ('mktg', 'Marketing')
    depts = db.session.query(Department.dept_code, Department.dept_name)
    form.dept_code.choices = depts
    if form.validate_on_submit():
        name = form.name.data
        state = form.state.data
        dept_code = form.dept_code.data

        new_employee = Employee(name=name, state=state, dept_code=dept_code)
        db.session.add(new_employee)
        db.session.commit()
        
        return redirect('/phones')
    else:
        return render_template('add_employee_form.html', form=form)

@app.route('/employees/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    employee = Employee.query.get_or_404(user_id)
    # obj=employee prepopulates fields automatically based on employee data
    form = EmployeeForm(obj=employee)

    depts = db.session.query(Department.dept_code, Department.dept_name)
    form.dept_code.choices = depts

    if form.validate_on_submit():
        employee.name = form.name.data
        employee.state = form.state.data
        employee.dept_code = form.dept_code.data

        db.session.commit()
        return redirect('/phones')
    else:
        return render_template('edit_employee_form.html', form=form)
