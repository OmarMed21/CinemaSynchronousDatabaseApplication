## Author / Developer : Omar Medhat Aly 
## Date Created: 07.05.2023 - 17:25
## Last Date Modified : 09.05.2023
## Organization : Upwork

import re
import random

def has_integer(inputString) -> bool:
    return bool(re.search(r'\d', inputString))

def generate_ID(length):
    """
    Use This Function to Generate random IDs from Integers

    Args:
    ----
        length: The Number of Characters of the generated ID

    Returns:
    --------
        Generated ID with specific Length
    """
    numbers = 'abcdefghijklmnopqrstuvwxyz1234567890'
    result_str = ''.join(random.choice(numbers) for i in range(length))
    return result_str

"""Customers"""

class Customer:
    def __init__(self, ID:str, Name:str) -> None:
        """
        Args:
        ----
            - ID: The User should enter the Id 
            - Name: The name of the Movie
        """
        self.id = ID
        self.name =Name

    def get_discount(self, cost=0):
        self._cost = cost
        return self._cost
    
    
    def get_booking_fee(self, ticket_quantity):
        """
        Returns The Booking Fee ($) which's the Number of Tickets * 2$
        """
        self.quantity = ticket_quantity
        return self.quantity * 2
    
    def display_info(self):
        """Returns the ID , NAME & Ticket Quantity"""
        print(f"\nCustomer Details:")
        print("-----------------")
        print(F"ID: {self.id}\nName: {self.name}\nTicket's Quantity: {self.quantity}\nTotal Booking Fee added: {self.get_booking_fee(self.quantity)} $")

class RewardFlatCustomer:
    def __init__(self, discount_rate:float = 0.2) -> None:
        """
        Args:
        ----
            discount_rate : The Amount of the Discount for the Rewared Customers
        """
        self.discount = discount_rate

    def get_discount(self, cost):
        """Enter the Cost of the Ticket ($) and returns the Price with the Discount applied"""
        self.cost = cost
        return round(self.cost * self.discount, 3)
    
    def display_info(self):
        """Displays the Attributes"""
        print(F"\nDiscount: {self.discount * 100} %\nCost After Discount Applied: {self.get_discount(self.cost)} $\n")

    def set_discount_rate(self, new_discount_rate):
        """Enter the New Discount Rate that Your are willing to apply"""
        self.discount = new_discount_rate
        return self.discount

class RewardStepCustomer:
    def __init__(self, discount_rate=0.3) -> None:
        self.thresh = 50 ## 50$ as a Threshold
        self.discount_rate = discount_rate # 30% discount rate 

    def get_discount(self, cost):
        """Enter the Cost of the Ticket ($) and returns the Price with the Discount applied"""
        self.cost = cost
        if self.cost >= self.thresh : return round(self.cost * self.discount_rate, 3)
        else: return self.cost
        
    def display_info(self):
        """Displays the Attributes"""
        if self.cost >= self.thresh : print(F"\nDiscount: {self.discount_rate * 100} %\nCost After Discount Applied: {self.get_discount(self.cost)} $\n")
        else: print(f"\nSorry You Cann't receive a Discount because you didn't meet the Threshold\nCost : {self.get_discount(self.cost)} $\n")

    def set_discount_rate(self, new_discount_rate:float):
        """Enter the New Discount Rate that Your are willing to apply in %"""
        self.discount_rate = new_discount_rate
        return self.discount_rate
    
    def set_threshold(self, new_threshold):
        """Enter the New Threshold Rate that Your are willing to apply in $"""
        self.thresh = new_threshold
        return self.thresh

"""Movies"""  

class Movie:

    movies = {"Movies": [], "IDs": []} ## The dictionary of the Movies 

    def __init__(self):
        self.num_seats = 50

    def add_movie(self, name:str, ID):
        self.name = name ## The Name of the Movies
        self.id = ID
        if self.name not in self.__class__.movies['Movies']:
            if self.num_seats != 0:
                if has_integer(self.name): 
                    print("Movies should not contain Integers")
                    return None
                else:
                    self.__class__.movies['Movies'].append(self.name)
                    self.__class__.movies['IDs'].append(self.id)
                self.num_seats -= 1 ## just to calculate the rest number of seats
            else:
                print("Sorry we can't add more Movies\nThere's no more available Seats") 
        else: print('You have already entered that Movie Before')

    def seat_available(self):
        if self.num_seats == 1: 
            print(f"There is only {self.num_seats} Seat Availabe")
        elif self.num_seats > 1: 
            print(f"There are {self.num_seats} Seats Availabe")
        else: 
            print("There are is no more Seats")

    def display_info(self):
        print('\n')
        print("-"*39)
        print(f"| Total Number Of Seats Available: {self.num_seats} |")
        print("-"*39)
        rng = range(len(self.__class__.movies['Movies']))
        for _, i in zip(self.__class__.movies['Movies'], rng):
            print(f"\nMovie:")
            print("------")
            print(f"Movie: {self.__class__.movies['Movies'][i]}\nID: {self.__class__.movies['IDs'][i]}")
            i -=1

    def set_number_seats(self, new_num_seats:int):
        self.num_seats = new_num_seats
        return self.num_seats
    
"""Tickets"""

class Ticket:

    tickets = {"Tickets": [], "IDs": [], "Prices": []} ## The dictionary of the Movies 
    
    def add_ticket(self, name:str, ID, price:int):
        self.name = name ## Choose ticket Type
        self.id = ID
        self.price = int(price)
        if self.name not in self.__class__.tickets['Tickets']:
            if has_integer(self.name): 
                print("Ticket Types should not contain Integers")
                return None
            else:
                self.__class__.tickets['Tickets'].append(self.name)
                self.__class__.tickets['IDs'].append(self.id)
                self.__class__.tickets['Prices'].append(self.price)
        else: print("\nThis Ticket is already booked")

    def display_info(self):
        rng = range(len(self.__class__.tickets['Tickets']))
        for _, i in zip(self.__class__.tickets['Tickets'], rng):
            print(f"\nTicket:")
            print("-------")
            print(f"Ticket Type: {self.__class__.tickets['Tickets'][i]}\nID: {self.__class__.tickets['IDs'][i]}\nPrice: {self.__class__.tickets['Prices'][i]} $")
            i -=1

"""Bookings"""

class Booking:

    reward_types = ['flat', 'step']

    def __init__(self, 
                 customer_name:str, 
                 movie_name, 
                 ticket_type, 
                 tikcet_price, 
                 quantity, 
                 customer_id=None, 
                 movie_id=None, 
                 ticket_id=None,
                 rewared_type=None, 
                 discount_rate=None,
                 thresh=None,
                 NUM_SEATS:int=50):
        self.customer_id = customer_id
        if self.customer_id is None: self.customer_id = generate_ID(2) ## if the user never added an id it will automaticall generate one
        self.customer = Customer(self.customer_id, customer_name)

        self.movie_name=  movie_name
        self.movie_id=  movie_id
        if self.movie_id is None : self.movie_id = generate_ID(2) ## if the user never added an id it will automaticall generate one

        self.ticket_name = ticket_type
        self.ticket_id = ticket_id
        if self.ticket_id is None: self.ticket_id = generate_ID(2) ## if the user never added an id it will automaticall generate one
        self.ticket_price = tikcet_price
        self.quantity = quantity

        self.thresh = thresh
        self.discount_rate = discount_rate
        self.reward_type = rewared_type
        if self.reward_type is not None:
             if self.reward_type not in self.reward_types: 
                 print("There's something Wrong\nyou should only choose [flat / step]")
             elif self.reward_type == 'flat':
                 if self.discount_rate is not None: self.reward = RewardFlatCustomer(discount_rate=self.discount_rate)
                 else: 
                     self.reward = RewardFlatCustomer() ## will be set as default
                     self.discount_rate = 0.2
             elif self.reward_type == 'step': 
                 if self.discount_rate is not None:
                     self.reward= RewardStepCustomer(discount_rate=self.discount_rate)
                     if self.thresh is not None: self.reward.set_threshold(new_threshold=self.thresh)
                 else: 
                     self.reward = RewardStepCustomer() ## will be set as default
                     self.discount_rate = 0.3
                     if self.thresh is not None: self.reward.set_threshold(new_threshold=self.thresh)
                     else:
                         self.thresh = 50

        self.num_seats = NUM_SEATS

    def display_info(self):
        ticket = Ticket()
        movie = Movie()

        self.customer.get_booking_fee(self.quantity)
        ticket.add_ticket(self.ticket_name, self.ticket_id, self.ticket_price)
        movie.set_number_seats(self.num_seats)
        movie.add_movie(self.movie_name, self.movie_id)

        self.customer.display_info()
        ticket.display_info()
        movie.display_info()

    def compute_cost(self):
        total_cost = self.quantity * self.ticket_price
        print('\n')
        print("The Cost: ")
        print("-"*9)
        print(
            f"Total cost: {total_cost} $\nTotal Booking Fee: {self.quantity * 2} $\nPrice after Discount: {total_cost * self.discount_rate} $"
        )

"""Records"""

class Records: 
    customers = {
    'customer_id': [],
    'customer_name': [],
    'discount_rate': [],
    'threshold': [] }  

    movies = {
        'movie_id': [],
        'movie_name': [],
        'num_seats': [] } 

    tickets = {
        'ticket_id': [],
        'ticket_type': [],
        'ticket_unit_price': [] }
    
    def add_customer(self, 
                 customer_id, 
                 customer_name, 
                 discount_rate="", 
                 threshold=""):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__discount_rate = discount_rate
        self.__thresh = threshold

        if self.__customer_id not in self.customers['customer_id']: self.__class__.customers['customer_id'].append(self.__customer_id)
        if self.__customer_name not in self.customers['customer_name']: self.__class__.customers['customer_name'].append(self.__customer_name)
        self.__class__.customers['discount_rate'].append(self.__discount_rate)
        self.__class__.customers['threshold'].append(self.__thresh)

    def add_movie(self, 
                 movie_id, 
                 movie_name, 
                 num_seats=""):
        self.__movie_id = movie_id
        self.__movie_name = movie_name
        self.__num_seats = num_seats

        if self.__movie_id not in self.movies['movie_id']: self.__class__.movies['movie_id'].append(self.__movie_id)
        if self.__movie_name not in self.movies['movie_name']: self.__class__.movies['movie_name'].append(self.__movie_name)
        self.__class__.movies['num_seats'].append(self.__num_seats)

    def add_ticket(self, 
                 ticket_id, 
                 ticket_type, 
                 ticket_unit_price=""):
        self.__ticket_id = ticket_id
        self.__ticket_type = ticket_type
        self.__ticket_unit_price = ticket_unit_price

        if self.__ticket_id not in self.tickets['ticket_id']: self.__class__.tickets['ticket_id'].append(self.__ticket_id)
        if self.__ticket_type not in self.tickets['ticket_type']: self.__class__.tickets['ticket_type'].append(self.__ticket_type)
        self.__class__.tickets['ticket_unit_price'].append(self.__ticket_unit_price)

    def read_customers(self):
        MAX_LEN = len(self.customers['customer_id'])
        LEN_DIS = len(self.customers['discount_rate'])
        LEN_THRESH = len(self.customers['threshold'])

        for _ in range(MAX_LEN - LEN_THRESH):
            self.customers['threshold'].append("")
        for _ in range(MAX_LEN - LEN_DIS):
            self.customers['discount_rate'].append("")

        x = self.customers['customer_id']
        y = self.customers['customer_name']
        z = self.customers['discount_rate']
        t = self.customers['threshold']

        with open(r"E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\customers.txt", "w", encoding='utf-8') as f:
            for x_, y_, z_, t_ in zip(x, y, z, t):
                if t_ == "" and z_ == "": f.write(x_+", "+ y_ +'\n')
                elif t_ == "" and z != "": f.write(x_+", "+ y_+", "+str(z_)+'\n')
                else: f.write(x_+", "+ y_+", "+str(z_) +", "+ str(t_)+'\n')

    def read_movies(self):
        MAX_LEN = len(self.movies['movie_id'])
        LEN_SEATS = len(self.movies['num_seats'])

        for _ in range(MAX_LEN - LEN_SEATS):
            self.movies['num_seats'].append("")

        x = self.movies['movie_id']
        y = self.movies['movie_name']
        z = self.movies['num_seats']

        with open(r"E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\movies.txt", "a", encoding='utf-8') as f:
            for x_, y_, z_ in zip(x, y, z):
                if z_ == "": f.write(x_+", "+ y_ +'\n')
                else: f.write(x_+", "+ y_+", "+str(z_) +'\n')

    def read_tickets(self):
        MAX_LEN = len(self.tickets['ticket_id'])
        LEN_UNIT_PRICE = len(self.tickets['ticket_unit_price'])

        for _ in range(MAX_LEN - LEN_UNIT_PRICE):
            self.tickets['ticket_unit_price'].append("")

        x = self.tickets['ticket_id']
        y = self.tickets['ticket_type']
        z = self.tickets['ticket_unit_price']

        with open(r"E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\tickets.txt", "w", encoding='utf-8') as f:
            for x_, y_, z_ in zip(x, y, z):
                if z_ == "": f.write(x_+", "+ y_ +'\n')
                else: f.write(x_+", "+ y_+", "+str(z_) +'\n')

    def find_customer(self, by, value):
        """
        by: what do you want to search by [id / name]
        value: the id / name of the customer 
        """
        if by == 'id':
            lst_ids = self.customers['customer_id']
            if value in lst_ids:
                print('Customer Found Successfully..')
                idx = lst_ids.index(value)
                print(f"Customer's Name: {self.customers['customer_name'][idx]}\nCustomer's ID: {self.customers['customer_id'][idx]}")
            else:
                print('Unfortunately The Customer not found by the Given Data')

        elif by == 'name':
            lst_names = self.customers['customer_name']
            if value in lst_names:
                print('Customer Found Successfully..')
                idx = lst_names.index(value)
                print(f"Customer's Name: {self.customers['customer_name'][idx]}\nCustomer's ID: {self.customers['customer_id'][idx]}")
            else:
                print('Unfortunately The Customer not found by the Given Data')

        else:
            print("There's no other Method ... [ID / NAME]")
    
    def find_ticket(self, by, value):
        if by == 'ticket_id':
            lst_ids = self.tickets['ticket_id']
            if value in lst_ids:
                print('Ticket Found Successfully..')
                idx = lst_ids.index(value)
                print(f"Ticket's ID: {self.tickets['ticket_id'][idx]}\nTicket's Type: {self.tickets['ticket_type'][idx]}")
            else:
                print('Unfortunately The Ticket not found by the Given Data')

        elif by == 'ticket_type':
            lst_types = self.tickets['ticket_type']
            if value in lst_types:
                print('Ticket Found Successfully..')
                idx = lst_types.index(value)
                print(f"Ticket's ID: {self.tickets['ticket_id'][idx]}\nTicket's Type: {self.tickets['ticket_type'][idx]}")
            else:
                print('Unfortunately The Ticket not found by the Given Data')

        else:
            print("There's no other Method ... [TICKET ID / TICKET TYPE]")

    def find_movie(self, by, value):
        if by == 'movie_id':
            lst_ids = self.movies['movie_id']
            if value in lst_ids:
                print('Movie Found Successfully..')
                idx = lst_ids.index(value)
                print(f"Movie's ID: {self.movies['movie_id'][idx]}\nMovie's Name: {self.movies['movie_name'][idx]}")
            else:
                print('Unfortunately The Movie not found by the Given Data')

        elif by =='movie_name':
            lst_names = self.movies['movie_name']
            if value in lst_names:
                print('Movie Found Successfully..')
                idx = lst_names.index(value)
                print(f"Movie's ID: {self.movies['movie_id'][idx]}\nMovie's Name: {self.movies['movie_name'][idx]}")
            else:
                print('Unfortunately The Movie not found by the Given Data')

        else:
            print('Unfortunately The Movie not found by the Given Data')

    def display_customers(self):
        x = self.customers['customer_id']
        y = self.customers['customer_name']
        z = self.customers['discount_rate']
        t = self.customers['threshold']
        rng = range(len(x))
        for x_, y_, z_, t_, idx in zip(x, y, z, t, rng):
            print("-"*50)
            print("-"*17)
            print(f"| Customer {idx +1} Info |")
            print("-"*17)
            if t_== "" and z_ == "": 
                print(f"Customer Name: {y_}\nCustomer ID: {x_}")
            elif t_ == "" and z != "":
                print(f"\nThat Customer is ==> [ Reward Flat Customer ] <==\n\nCustomer Name: {y_}\nCustomer ID: {x_}\nDiscount Rate: {z_}")
            else:
                print(f"\nThat Customer is ==> [ Reward Step Customer ] <==\n\nCustomer Name: {y_}\nCustomer ID: {x_}\nDiscount Rate: {z_}\nThreshold Cost: {t_}")
            print("-"*50)
            print('\n')

    def display_tickets(self):
        x = self.tickets['ticket_id']
        y = self.tickets['ticket_type']
        z = self.tickets['ticket_unit_price']
        rng = range(len(x))
        for x_, y_, z_, idx in zip(x, y, z, rng):
            print("-"*50)
            print("-"*17)
            print(f"| Ticket {idx+1} Info |")
            print("-"*17)
            print(f"Ticket Type: {y_}\nTicket ID: {x_}\nTicket Unit Price: {z_} $")
            print("-"*50)
            print('\n')

    def display_movies(self):
        x = self.movies['movie_id']
        y = self.movies['movie_name']
        z = self.movies['num_seats']
        rng = range(len(x))
        for x_, y_, z_, idx in zip(x, y, z, rng):
            print("-"*50)
            print("-"*17)
            print(f"| Movie {idx + 1} Info |")
            print("-"*17)
            print(f"Movie Name: {y_}\nMovie ID: {x_}\nNumber of Seats: {z_}")
            print("-"*50)
            print('\n')
    
class GroupTicket(Records):

    Records.tickets.update(ticket_1=[])
    Records.tickets.update(quantity_1=[])
    Records.tickets.update(ticket_2=[])
    Records.tickets.update(quantity_2=[])
    Records.tickets.update(ticket_3=[])
    Records.tickets.update(quantity_3=[])

    def add_group_ticket(self,
                groupTicket_ID,
                groupTicket_name,
                ticket_1,
                quantity_1,
                ticket_2="",
                quantity_2="",
                ticket_3="",
                quantity_3=""):
        self.groupTicket_ID = groupTicket_ID
        self.groupTicket_name = groupTicket_name
        self.ticket_1 =  ticket_1
        self.ticket_2 =  ticket_2
        self.ticket_3 =  ticket_3
        self.quantity_1 = quantity_1
        self.quantity_2 = quantity_2
        self.quantity_3 = quantity_3

        super(GroupTicket, self).tickets['ticket_id'].append(self.groupTicket_ID)
        super(GroupTicket, self).tickets['ticket_type'].append(self.groupTicket_name)
        super(GroupTicket, self).tickets['ticket_1'].append(self.ticket_1)
        super(GroupTicket, self).tickets['quantity_1'].append(self.quantity_1) 
        super(GroupTicket, self).tickets['ticket_2'].append(self.ticket_2)
        super(GroupTicket, self).tickets['quantity_2'].append(self.quantity_2)
        super(GroupTicket, self).tickets['ticket_3'].append(self.ticket_3)
        super(GroupTicket, self).tickets['quantity_3'].append(self.quantity_3)

    def display(self):
        print(super(GroupTicket, self).tickets)

    def read_group_tickets(self):
        x = self.tickets['ticket_id']
        y = self.tickets['ticket_type']
        z = self.tickets['ticket_unit_price']

        LEN_X = len(x)
        LEN_Y = len(y)
        LEN_Z = len(z)
        MAX_LEN = 6

        for _ in range(MAX_LEN - LEN_X):
            x.append("")
        for _ in range(MAX_LEN - LEN_Y):
            y.append("")
        for _ in range(MAX_LEN - LEN_Z):
            z.append("")
        
        t1 = self.tickets['ticket_1']
        for _ in range(MAX_LEN - len(t1)):
            t1.append("")
        t2 = self.tickets['ticket_2']
        for _ in range(MAX_LEN - len(t2)):
            t2.append("")
        t3 = self.tickets['ticket_3']
        for _ in range(MAX_LEN - len(t3)):
            t3.append("")
        q1 = self.tickets['quantity_1']
        for _ in range(MAX_LEN - len(q1)):
            q1.append("")
        q2 = self.tickets['quantity_2']
        for _ in range(MAX_LEN - len(q2)):
            q2.append("")
        q3 = self.tickets['quantity_3']
        for _ in range(MAX_LEN - len(q3)):
            q3.append("")

        with open(r"E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\tickets_group.txt", "a", encoding='utf-8') as f:
            for x_, y_, t1_, q1_, t2_, q2_, t3_, q3_ in zip(x, y, t1, q1 ,t2, q2, t3, q3):
                if (t2_ == "" and q2_ == "") or (t3_ == "" and q3_ == ""): f.write(x_ + ", " + y_+", " +t1_ + ", " +str(q1_)+ '\n')
                elif t3_ == "" and q3_ == "": f.write(x_ + ", "+ y_+", " +t1_ + ", " +str(q1_)+ ", "+ t2_ + ", "+str(q2_)+'\n')
                else: f.write(x_ + ", "+ y_+", " +t1_ + ", " +str(q1_)+ ", "+ t2_ + ", "+str(q2_)+ ", " + t3_+ ", "+ str(q3_) +'\n')
            



        













