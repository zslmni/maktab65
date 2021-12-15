from file_handler import *


class Person:
    def __init__(self):
        self.username = ''
        self.first_name = ''
        self.last_name = ''
        self.password = ''

    def sign_up(self):#sign up for first time
        admin_or_customer = input('1- Admin\n2- Customer')
        if admin_or_customer == '1':
            print('signed up ')

        elif admin_or_customer == '2':
            print('signed up')

    def search_admin(self):#search admin information in admin file
        print('admin info')

    def search_customer(self):#search customer information in customer file
        print('customer info')
