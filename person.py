import pandas as pd
from file_handler import *
import log


class Person:
    def __init__(self , username , password):
        self.username = username
        self.password = password
        
    
    
    def admin_sign_in(self):#this instance make a csv file of admins username and pass
        ob = FileHandler('admin_file.csv')
        ob.write_file({'user_name':self.username , 'password':self.password })
        

    def customer_sign_in(self):#making a csv file of costomer information
        ob = FileHandler('customer_file.csv')
        ob.write_file({'user_name':self.username , 'password':self.password })

        
    @classmethod
    def admin_log_in(cls, username , password):
        df = pd.read_csv('admin_file.csv')
        if username in df['user_name'].values and password in df['password'].values:
            print('successfully log in')
            return True
        else:
            print('username or password incorrect!')
            log.warning_logger.error(f"User with username : {username} doesn't exist.")
            return False


    @classmethod
    def customer_log_in(cls , username , password):
        df = pd.read_csv('customer_file.csv')
        if username in df['user_name'].values and password in df['password'].values:
            print('successfully log in')
            return True
        else:
            print('username or password incorrect!')
            log.warning_logger.error(f"User with username : {username} doesn't exist.")
            return False


def make_person():
    enterance = input('Are you   1-Admin   2-Customer\n ')
    if enterance == '1':
        admin_code = input('Enter your admin code:\n')
        if admin_code in ['zslmni', 'zahra' , 'salamni']:
            username = input('Enter your user name:\n')
            password = input('Enter your password:\n')
            admin = Person(username , password)
            admin.admin_sign_in()
            print('Welcome!successfully signed up!')
        else:
            print('your admin code was invalid!')

    elif enterance == '2':
            username = input('Enter your user name:\n')
            password = input('Enter your password:\n')
            customer = Person(username, password)
            customer.customer_sign_in()
            print('Welcome!successfully signed up!')
    return  username , password
