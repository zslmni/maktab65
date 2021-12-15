class Event:

    '''define event by admin and buying ticket by customer'''

    def __init__(self, date_event , location , totall_ticket , remain_ticket , price , discount_code):
        self.date_event = date_event
        self.location = location
        self.totall_ticket = totall_ticket
        self.remain_ticket = remain_ticket
        self.price = price
        self.discount_code = discount_code

        def define_event(self):#define event by admin
            print('event defined')

        def show_event(self): #showing list of event by customer
            print("list of events: ")

        def choose_event(self): #choosing event by customer
            print("choose your event and how many ticket do you want")


        def input_discount_code(self): #enter discount code by customer
            print("discount code entered!")

        def show_price(self): #showing totall price
            print("price you should pay: ")

        def manage_ticket(self):#manage tickets by admin
            print('showing sold tickets and remain tickets')

        
