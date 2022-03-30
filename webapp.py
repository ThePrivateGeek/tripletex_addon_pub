import sys
from flask import Flask, request, render_template, url_for, redirect
import service


app = Flask(__name__)

@app.route('/')
def home():  
    global banner
    banner = get_banner()
    if service.client is None:     
        service.create_client() 
    return render_template('template.html', banner=banner)    

@app.route('/create_emps')
def create_emps():
    result = service.create_emps()
    return render_template('create_emps.html', result=result, banner=banner)

@app.route('/employees')
def employees():
    result = service.get_emps()
    return render_template('employees.html', result=result, banner=banner)

@app.route('/employees/<emp_id>')
def employee_details(emp_id):
    result = service.get_emp_details(emp_id).value
    return render_template('single_employee.html', result=result, banner=banner)


@app.route('/products')
def products():
    result = service.get_prods()
    return render_template('products.html', result=result, banner=banner)

@app.route('/products/<prod_id>')
def product_details(prod_id):
    result = service.get_prod_details(prod_id).value
    return render_template('single_product.html', result=result, banner=banner)

@app.route('/create_prod', methods=['GET','POST'])
def create_prod():
    if request.method == 'POST':
        prod_name = request.form['prod_name']
        result = service.create_product(prod_name)
        return render_template('create_prod.html', result=result, banner=banner)
    else:
        return render_template('create_prod.html', banner=banner)

@app.route('/projects')
def projects():    
    result = service.get_projects()
    return render_template('projects.html', result=result, banner=banner)

@app.route('/create_project', methods=['GET','POST'])
def create_project():
    if request.method == 'POST':
        project_name = request.form['project_name']
        result = service.create_project(project_name)
        return render_template('create_project.html', result=result, banner=banner)
    else:
        return render_template('create_project.html', banner=banner)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/redirect/')
def redirect_url():
    companyId = request.args.get('companyId')
    companyName = request.args.get('companyName')
    token = request.args.get('token')
    with open('config.txt', 'w') as config_file:
        config_file.write(f'companyId:{companyId}\n')
        config_file.write(f'companyName:{companyName}\n')
        config_file.write(f'employeeToken:{token}')
    return redirect('/login')


def get_banner():
    sys.stdout.write(">>>> INSIDE get banner\n")
    with open('config.txt', 'r') as config_file:
        lines = config_file.readlines()
        company_id = lines[0].split(':')[1]
        company_name = lines[1].split(':')[1]
        banner = f'... TPG {company_name} ({company_id})'
        sys.stdout.write(">>>> banner:" + banner + "\n")
        return banner


if (__name__ == '__main__'):
    app.run(debug=False)