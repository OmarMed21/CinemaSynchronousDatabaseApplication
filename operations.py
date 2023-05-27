from utils import *
import sys
import pandas as pd

r = Records()

index_col_movies=["ID", "Movie Name", "Seats available"]
index_col_tickets=["ID", "Ticket Type", "Ticket Unit Price"]
index_col_customers=["ID", "Customer Name", "Discount", "Threshold"]
index_col_tickets_g=["ID", "Ticket Type", "Ticket Unit Price", "Ticket 1", "Quantity 1", "Ticket 2", "Quantity 2", "Ticket 3"]
index_col_bookings=["Customer Name/ID", "Movie Name/ID", "Ticket 1 type Name/ID", "Ticket 1 Quantity", "Ticket 2 type Name/ID", "Ticket 2 Quantity", "Discount", "Booking Fee", "Total Cost"]

DEFAULT_DISCOUNT_REWARD_FLAT_CUSTOMER = RewardFlatCustomer(0.2).discount
DEFAULT_DISCOUNT_REWARD_STEP_CUSTOMER = RewardStepCustomer(0.3).discount_rate

movies_df = pd.read_table(r"E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\movies.txt",
                    delimiter=", ",
                    header=None,
                    names=index_col_movies)

tickets_df = pd.read_table(r"E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\tickets.txt",
                    delimiter=", ",
                    header=None,
                    names=index_col_tickets)


customers_df = pd.read_table(r"E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\customers.txt",
                    delimiter=", ",
                    header=None,
                    names=index_col_customers)

tickets_df_g = pd.read_table(r"E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\tickets_group.txt",
                    delimiter=", ",
                    header=None,
                    names=index_col_tickets_g)

bookings_df = pd.read_table(r"E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\bookings.txt",
                    delimiter=", ",
                    header=None,
                    names=index_col_bookings)

bookings_df.fillna("UNKOWN", inplace=True)
customers_df.fillna(0, inplace=True)

movies_names = list(movies_df['Movie Name'])
tickets_types = list(tickets_df_g['Ticket Type'])
tickets_unit_prices = list(tickets_df['Ticket Unit Price'])
customers_names = list(customers_df['Customer Name'])

def find_price_group(ticket_type:str):
    type1 = tickets_df_g[tickets_df_g['Ticket Type'] == ticket_type].iloc[0, :]['Ticket Unit Price']
    quan1 = int(tickets_df_g[tickets_df_g['Ticket Type'] == ticket_type].iloc[0, :]['Ticket 1'])

    if 'T' in type1:
        v_1 = tickets_df_g[tickets_df_g['ID'] == type1]['Ticket Unit Price']
    else: v_1 = tickets_df_g[tickets_df_g['Ticket Type'] == type1]['Ticket Unit Price']

    type2 = tickets_df_g[tickets_df_g['Ticket Type'] == ticket_type].iloc[0, :]['Quantity 1']
    type3 = tickets_df_g[tickets_df_g['Ticket Type'] == ticket_type].iloc[0, :]['Quantity 2']

    if type2 == None and type3 == None:
        output = (float(v_1) * quan1) * .8
        
    elif type2 != None and type3 == None:
        if 'T' in type2:
            v_2 = tickets_df_g[tickets_df_g['ID'] == type2]['Ticket Unit Price']
        else: v_2 = tickets_df_g[tickets_df_g['Ticket Type'] == type2]['Ticket Unit Price']

        quan2 = int(tickets_df_g[tickets_df_g['Ticket Type'] == ticket_type].iloc[0, :]['Ticket 2'])
        output = (float(v_1) * quan1 + float(v_2) * quan2) * .8

    else:
        if 'T' in type2:
            v_2 = tickets_df_g[tickets_df_g['ID'] == type2]['Ticket Unit Price']
        else: v_2 = tickets_df_g[tickets_df_g['Ticket Type'] == type2]['Ticket Unit Price']

        if 'T' in type3:
            v_3 = tickets_df_g[tickets_df_g['ID'] == type3]['Ticket Unit Price']
        else: v_3 = tickets_df_g[tickets_df_g['Ticket Type'] == type3]['Ticket Unit Price']

        quan2 = int(tickets_df_g[tickets_df_g['Ticket Type'] == ticket_type].iloc[0, :]['Ticket 2'])
        quan3 = int(tickets_df_g[tickets_df_g['Ticket Type'] == ticket_type].iloc[0, :]['Ticket 3'])

        output =  (float(v_1) * quan1 + float(v_2) * quan2 + float(v_3) * quan3) * .8

    return output

def represent_all(x):
    def represent_data(x):
        for i in range(len(x) -1):
            if x[i] != "UNKOWN": 
                print(str(x[i])+ ", ", end='')
                
        if x[-1] != "UNKOWN": 
            print(f"{x[-1]}", end='')

    for i in range(len(bookings_df)):
        x = bookings_df.iloc[i, :]
        represent_data(x=x)
        print('')

def most_popular_movie():
    dic = {"Movie/ID": [], "Total Cost": []}
    movies_ids = list(movies_df['ID'])

    for i in range(len(bookings_df)):
        if (bookings_df.iloc[i, :][-1] and bookings_df.iloc[i, :][-2]) == 'UNKOWN':
            dic["Movie/ID"].append(bookings_df.iloc[i, :][1])
            dic["Total Cost"].append(bookings_df.iloc[i, :][-3])
        elif (bookings_df.iloc[i, :][-1]) != 'UNKOWN' and (bookings_df.iloc[i, :][-2]) == 'UNKOWN':
            dic["Movie/ID"].append(bookings_df.iloc[i, :][1])
            dic["Total Cost"].append(bookings_df.iloc[i, :][-2])
        else:
            dic["Movie/ID"].append(bookings_df.iloc[i, :][1])
            dic["Total Cost"].append(bookings_df.iloc[i, :][-1])

    df = pd.DataFrame(dic)
    most_popular_movie = df[df['Total Cost'] == max(dic['Total Cost'])].iloc[0][0]
    if most_popular_movie in movies_ids:
        most_popular_movie =  movies_df[movies_df['ID'] == most_popular_movie]['Movie Name'].iloc[0]
    print(f"The Most Popular Movie is : {most_popular_movie}")

## the interface window and the Menu
print("#"*65)
print("You can choose from the following options:")
print("1: Purchase a Ticket")
print("2: Display existing customers’ information")
print("3: Display existing movies’ information")
print("4: Display existing ticket types’ information")
print("5: Add movies")
print("6: Adjust the discount rate of all RewardFlat customers")
print("7: Adjust the discount rate of a RewardStep customer")
print("8: Display all bookings")
print("9: Display the most popular movie")
print("10: Display all movie record")
print("0: Exit the program")
print("#"*65)
print("\n")

## The list of the menu
the_list_menu = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

## The input number will be stored in that string
input_entry = input("Choose one option: ")

if input_entry not in the_list_menu:
    print("That's not Valid, you should choose number from the List")
    print('\n')
    sys.exit()

if input_entry == "1": 
    name = input("Enter the name of the Customer [e.g. Huong]:\n")

    sit = True
    while sit:
        movie_name = input("Enter the name of the movie [enter a valid name only, e.g. Avatar]:\n")
        sit = False
        if movie_name not in movies_names:
            print("Movie is invalid, Please enter a valid movie!\n")
            sit = True

    sit = True
    while sit:
        ticket_type = str(input("Enter the ticket type [enter a valid type only, e.g. adult, child, senior]:\n"))
        sit = False
        if ticket_type not in tickets_types:
            print("Ticket Type is invalid, Please enter a valid ticket type!\n")
            sit = True

    quantity = int(input("Enter the ticket quantity [enter a positive integer only, e.g. 1, 2, 3]:\n"))

    sit = True
    while sit:
        program = input("The customer is not in the rewards program. Does the customer want to join the rewards program [enter y or n]?\n")
        sit = False
        if program not in ['y', 'n']:
            print("Not invalid answer, Please enter a valid answer [y / n] !\n")
            sit = True
    if 'G' in str(tickets_df_g[tickets_df_g['Ticket Type'] == ticket_type]['ID']):
        tickets_unit_price = find_price_group(ticket_type)
    else: tickets_unit_price = float(tickets_df[tickets_df['Ticket Type'] == ticket_type]['Ticket Unit Price'])
    
    booking_fee = quantity * 2
    if program == 'y':
        sit = True
        while sit:
            reward_type = input("What kind of rewards the customer wants?\n")            
            sit = False
            if reward_type not in ['F', 'S']:
                print("Not invalid answer, Please enter a valid answer [F / S] !\n")
                sit = True
        print("Successfully add the customer to the rewards program.")

        if reward_type == 'F':
            if name in customers_names:
                if float(customers_df[customers_df['Customer Name'] == name]['Discount']) == 0:
                    discount = round(DEFAULT_DISCOUNT_REWARD_FLAT_CUSTOMER * tickets_unit_price * quantity, 2)
                else:
                    discount = round(float(customers_df[customers_df['Customer Name'] == name]['Discount']) * tickets_unit_price * quantity, 2)
            else: discount = round(DEFAULT_DISCOUNT_REWARD_FLAT_CUSTOMER * tickets_unit_price * quantity, 2)
        
        if reward_type == 'S':
            if name in customers_names:
                if float(customers_df[customers_df['Customer Name'] == name]['Discount']) == 0:
                    discount = round(DEFAULT_DISCOUNT_REWARD_STEP_CUSTOMER * tickets_unit_price * quantity, 2)
                else:
                    discount = round(float(customers_df[customers_df['Customer Name'] == name]['Discount']) * tickets_unit_price * quantity, 2)
            else: discount = round(DEFAULT_DISCOUNT_REWARD_STEP_CUSTOMER * tickets_unit_price * quantity, 2)

        total_cost = booking_fee + quantity * tickets_unit_price - discount
        print('\n')
        print("-"*40)
        print(f"Receipt of {name}")
        print("-"*40)
        print("Movie:" + " "*27 + f"{movie_name}")
        print("Ticket Type:" + " "*22 + f"{ticket_type}")
        print("Ticket Unit Price:" + " "*17 + f"{str(tickets_unit_price)}")
        print("Ticket Quantity:" + " "*22 + f"{str(quantity)}")
        print("-"*40)
        print("Discount:" + " "*26 + f"{str(discount)}")
        print("Booking fee:" + " "*26 + f"{str(booking_fee)}")
        print("Total cost:" + " "*24 + f"{str(total_cost)}")

    elif program == 'n':
        total_cost = booking_fee + quantity * tickets_unit_price
        print('\n')
        print("-"*40)
        print(f"Receipt of {name}")
        print("-"*40)
        print("Movie:" + " "*27 + f"{movie_name}")
        print("Ticket Type:" + " "*22 + f"{ticket_type}")
        print("Ticket Unit Price:" + " "*17 + f"{str(tickets_unit_price)}")
        print("Ticket Quantity:" + " "*22 + f"{str(quantity)}")
        print("-"*40)
        print("Booking fee:" + " "*26 + f"{str(booking_fee)}")
        print("Total cost:" + " "*24 + f"{str(total_cost)}")

if input_entry == "2":
    print(customers_df.T)

if input_entry == "3":
    print(movies_df.T)

if input_entry == "4":
    print(tickets_df.T)

if input_entry == "5":
    movies = input("Enter the list of movies to be added (separating by commas):\n").split(', ')
    dic = {'ID': [], 'Movie Name': [], 'Seats available':[]}

    for i in range(len(movies)):
        if movies[i] in list(movies_df['Movie Name']):
            print(f"The movie {movies[i]} is an existing movie, will do nothing.")
            i -=1
        else:
            print(f"Adding the movie {movies[i]} ...")
            id_ = f"M{int(list(movies_df['ID'])[-1][-1]) + 1 + i}"
            dic['ID'].append(id_)
            dic['Movie Name'].append(movies[i])
            dic['Seats available'].append(50)
            r.add_movie(id_, movies[i], 50)

    r.read_movies()
    df = pd.DataFrame(dic)
    m_c = pd.concat([movies_df, df]).reset_index(drop=True)

if input_entry == "6":
    new_r = float(input('Enter the new discount rate of all RewardFlat customers [e.g. 0.2 ==> 20%] :\n'))
    DEFAULT_DISCOUNT_REWARD_FLAT_CUSTOMER.set_discount_rate(new_r)
    DEFAULT_DISCOUNT_REWARD_FLAT_CUSTOMER = DEFAULT_DISCOUNT_REWARD_FLAT_CUSTOMER.discount

if input_entry == "7":
    new_r = float(input('Enter the new discount rate of RewardStep customers [e.g. 0.2 ==> 20%] :\n'))
    DEFAULT_DISCOUNT_REWARD_STEP_CUSTOMER.set_discount_rate(new_r)
    DEFAULT_DISCOUNT_REWARD_STEP_CUSTOMER = DEFAULT_DISCOUNT_REWARD_STEP_CUSTOMER.discount_rate

if input_entry == "8":
    represent_all(bookings_df)

if input_entry == "9":
    most_popular_movie()

if input_entry == "10":
    pass

if input_entry == "0":
    sys.exit()