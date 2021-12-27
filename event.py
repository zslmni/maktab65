from file_handler import *


class Event:

    '''define event by admin and buying ticket by customer'''

    def __init__(self,event_name, date_event , location , totall_ticket , price  , discount_code = None , discount_percentage = None):
        self.event_name = event_name
        self.date_event = date_event
        self.location = location
        self.totall_ticket = totall_ticket
        self.remain_ticket = totall_ticket
        self.price = price
        self.discount_code = discount_code
        self.discount_percentage = discount_percentage

    def define_event(self):#define event by admin
        ob = FileHandler('event_file.csv')
        ob.write_file({ 'event_name': self.event_name ,'date_event' : self.date_event , 'location' : self.location , 'totall_ticket' : self.totall_ticket ,'price' : self.price, 'remain_ticket' : self.remain_ticket , 'discount_code' : self.discount_code , 'discount_percentage' : self.discount_percentage })
            

    @classmethod
    def choose_event(cls,event_name, num_ticket ): #choosing event by customer
        ob = FileHandler('event_file.csv')
        i = 0 #for getting index of line
        for line in ob.read_file():
            i = i + 1
            if event_name == line['event_name']:
                
                while True:
                    if num_ticket < line['totall_ticket']:
                        totall_price = int(cls.price)*int(num_ticket)
                        print(f'Totall price is {totall_price}')

                        ob.edit_row('remain_ticket',  int(cls.totall_ticket)-int(num_ticket),  i )
                        return True
                    else:
                        return False
                    

    @classmethod
    def remain_ticket(cls):#manage tickets by admin
        ob = FileHandler('event_file.csv')
        for line in ob.read_file():
            print(line['event_name'] , line['remain_ticket'])

        






