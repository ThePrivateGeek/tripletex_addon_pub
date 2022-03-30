base_url = 'https://tripletex.no/v2'
consumer_token = '<CONSUMER TOKEN>'

employee_token = ''
expiration_date = '2023-01-01'

class Config():
    def __init__(self):
        with open('config.txt', 'r') as config_file:
            lines = config_file.readlines()
            employee_token = lines[2].split(':')[1]
        
        self.base_url = base_url
        self.consumer_token = consumer_token
        self.employee_token = employee_token
        self.expiration_date = expiration_date
