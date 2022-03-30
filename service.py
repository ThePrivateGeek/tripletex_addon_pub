import csv
import json
from tripletex import Tripletex
from config import Config

client = None

def create_client():
    config = Config()
    global client
    client = Tripletex(config.base_url, config.consumer_token, config.employee_token, config.expiration_date)
    return client
'''
Alternatively, you can create a client from config, like so:
client = Tripletex.from_config(config)
'''
def create_client_by_emp_token(employee_token):
    config = Config()
    global client
    client = Tripletex(config.base_url, config.consumer_token, employee_token, config.expiration_date)
    return client

def create_emps():
    result = []
    with open('employees.cvs', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:        
            print(f'\tcreating {row["firstname"]} {row["lastname"]} ...')
            payload = {
                'firstName': row["firstname"],
                'lastName': row["lastname"],
                'email': row["email"],
                'dateOfBirth': row["dateOfBirth"],
                'userType': row["userType"],
                'employments': [
                    {
                        'startDate': row["startDate"], 
                        'employmentDetails': [
                            {
                                'percentageOfFullTimeEquivalent': row["percentageOfFullTimeEquivalent"]
                            }
                        ]
                    }
                ]
            }
            
            result.append(client.create_employee(payload=payload))
    return result

def get_emps():
    return client.get_employees()

def get_emp_details(employee_id):
    return client.get_employee_by_id(employee_id)

def create_product(name):
    payload = {
        'name': name
    }
    return client.create_product(payload=payload)

def get_prods():
    return client.get_products()

def get_prod_details(prod_id):
    return client.get_product_by_id(prod_id)

def create_project(name):
    payload = {'name': name}
    return client.create_project(payload=payload)

def get_projects():
    return client.get_projects()

def create_customer(name):
    payload = {
        'name': name
    }
    return client.create_customer(payload=payload)

def create_order(customer_id, customer_name, product_id, order_date, delivery_date):
    payload = {
        'customer' : 
        {
            'id': customer_id,
            'name': customer_name
        },
        'orderLines': [
            {
                'product': 
                {
                    'id': product_id
                }  
            }
        ],
        'orderDate': order_date,
        'deliveryDate': delivery_date
    }
    return client.create_order(payload=payload)

def create_invoice(invoice_date, invoice_due_date, order_id):
    
    payload = {
        'invoiceDate': invoice_date,
        'invoiceDueDate': invoice_due_date,
        'orders': [{'id': order_id}]
    }
    return client.create_invoice(payload=payload)
