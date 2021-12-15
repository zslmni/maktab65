from define_role import *
from event import *
from logging import *
from file_handler import *

while True:
    input_role = input('1- Admin\n2- Customer\n')#detect admin and customer
    if input_role == '1':
        user_name = input('Enter your user name:\n')#loging in as admin
        
        while x > 0:
            password = input('Enter your password')
            if password not in admin_file:
                logging.warning('Invalid PASSWORD!!')
                x -= 1
        if user_name in admin_file:#finding admin information
            Event.define_event()
            Event.manage_ticket()
        else:
            print('invalid user name')

    elif input_role == '2':#customer part
        user_name = input('Do you have an account?\n1-log in\n2-sign up\n')
        if user_name == '1':#log in as customer
            while x > 0:
                password = input('Enter your password')
                if password not in admin_file:
                    logging.warning('Invalid PASSWORD!!')
                    x -= 1
            Event.show_event()
            Event.choose_event()
            Event.input_discount_code()
            Event.show_price()
        elif user_name == '2':#sign up as customer
            Person.sign_up()