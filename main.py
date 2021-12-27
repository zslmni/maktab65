from person import *
from event import *
from file_handler import *
import log




while True:
    enterance = input('Welcome! Are you:\n1-Admin\n2-Customer\n')
    if enterance == '1': 
################################# Staring admin part ####################################


        log_or_sign = input('Do you have an account? 1- log in 2- sign in\n')
        if log_or_sign == '1':#getting admin information for log in

            admin_username = input('Please enter your user name: ')
            admin_password = input('password: ')
            
            if Person.admin_log_in(admin_username, admin_password):
                 #every thing that admin can do

                while True:

                    admin_menu = input('what do you want to do?   1-Define Event  2-Remain ticket  ')

                    if admin_menu == '1':
                        event_name = input('please enter event information.\nEvent name:')
                        date_event = input( 'Data event: ')
                        location = input('Loction: ')
                        totall_ticket = input('Totall tickets: ')
                        price = input('Price: ')
                        discount_code , discount_percentage = input('If you want to define discount code enter the code and discount_percentage or ignor this: ').split(' ')
                        my_event = Event(event_name ,date_event, location, totall_ticket, price , discount_code , discount_percentage)

                    
                        my_event.define_event()
                        log.info_logger.info(f"{my_event} is created.")

                    elif admin_menu == '2':
                        Event.remain_ticket()
            
        elif log_or_sign == '2':# sign in as admin with admin code, user name and password
            make_person()

############################### Ending admin part #######################################



################################ Starting customer part #################################


    elif enterance == '2':
        while True:
            log_or_sign = input('Do you have an account? 1- log in 2- sign in\n')
            if log_or_sign == '1':#getting customer information for log in

                customer_username = input('Please enter your user name and password: ')
                customer_password = input('password: ')
                if Person.customer_log_in(username, password):

                    while True:
                        customer_menu = input('waht do you want to do?\n1-Show event\n2-choose event')

                        if customer_menu == '1':
                            ob = FileHandler('event_file.csv')
                            print(ob.read_file())

                        if customer_menu == '2':
                            event_name = input('enter name of event: ')
                            num_ticket = input('How many ticket do you want? ')
                            
                            Event.choose_event(event_name, num_ticket)



            elif log_or_sign == '2':
                make_person()