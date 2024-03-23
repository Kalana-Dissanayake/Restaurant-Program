class Menu:
    def __init__(self):

        # Initialize menu items and their prices.
        self.items = {
            "House Cured Bourbon Gravadlax": 9.99, 
            "Bloc de pate": 14.99, 
            "village market testing plate": 7.99, 
            "White's Out seafood cocktail": 14.99, 
            "Essex camembert souffle": 9.99,
            "Beef": 45.99, 
            "Steak Diane": 49.99, 
            "Lobster": 49.99, 
            "Rack of Welsh lamb": 24.99, 
            "pan fried cod loin": 24.99, 
            "Charred cauliflower steak": 29.99,
            "poached alice pears": 8.99, 
            "Apricot & brandy macaroon": 7.99, 
            "Floating island": 7.99, 
            "Dark chocolate & strawberry cheesecake": 8.99, 
            "Macadamia blondie & chocolate brownie": 5.99,
            "Coffee & biscuits": 5.99,
            "Wine": 8, 
            "Water": 1, 
            "Soda": 2
        }
         # Initialize a dictionary to track the popularity of each menu item.
        self.menu_popularity  = {item: 0 for item in self.items.keys()}

      # Method to print the menu popularity.
    def show(self):
        print(self.menu_popularity)

# Define a Table class to represent restaurant tables.
class Table:
    def __init__(self, table_no):
        self.table_no = table_no
        self.status = "Available"
        self.session = ""
        self.no_of_guests = 0
        self.orders = {}
        self.cost = 0
#Define the main program class for managing the restaurant.
class Program:
    def __init__(self):

        # Initialize data structures to manage tables, orders, and income.
        self.earlyses_tables = {i: {"status": "Available", "Session": "", "Number of Guests": 0, "orders": {}, "cost": 0} for i in range(1,6)}
        self.lateses_tables = {i: {"status": "Available", "Session": "", "Number of Guests": 0, "orders": {}, "cost": 0} for i in range(1,6)}
        self.earlyses_reserved_tables = []
        self.lateses_reserved_tables = []
        self.earlyses_order_items = {}
        self.lateses_order_items = {}
        self.priority_orders = []
        self.order_price = 0
        self.total_income = 0
        self.table_costs = {}
        self.total_tips = 0
        self.menu = Menu()# Create an instance of the Menu class to access menu items and popularity.

     # Method for placing an order and reserving a table.
    def place_order(self):
        global table
        sessions = ["1. Early Session", "2. Late session"]
        for i in range(len(sessions)):
            print(sessions[i])
        Session = int(input("Select Session: "))
        no_guest = int(input("Number of Guests: "))
        if 1 <= no_guest <= 8:
            if Session == 1:
                table_no = int(input("Enter Table Number: "))
                if table_no not in self.earlyses_reserved_tables:
                    table = self.earlyses_tables[table_no]
                    order_item = input("Enter the Item: ")
                    while order_item != "0":
                        p = int(input("Enter Portion: "))
                        self.earlyses_order_items[order_item] = p
                        order_item = input("Enter the Item: ")

                    for item in self.earlyses_order_items.keys():
                        if item in ["Lobster", "Steak Diane"]:
                            self.priority_orders.append(item)
                            self.order_price += self.menu.items[item] * self.earlyses_order_items[item]
                        self.menu.menu_popularity[item] += 1
                    table["orders"].update(self.earlyses_order_items)
                    table["Session"] = "Early Session"

                    tip = 0.05 * self.order_price

                    if len(self.earlyses_order_items) != 0:
                        print("Select Payment Method")
                        payment_methods = ["1. Pay with Visa/Master Card", "2. Pay with Cash"]
                        for i in range(len(payment_methods)):
                            print(payment_methods[i])
                        pay_method = int(input("Enter Payment Method: ")) 
                        if pay_method == 1:
                            self.order_price += self.order_price * 0.1
                        
                        print("Table Reserved Successfully")
                        table["status"] = "Reserved"
                        table["Number of Diners"] = no_guest
                        table["cost"] = f"${self.order_price}"

                    self.total_income += self.order_price
                    self.total_tips += tip
                    self.table_costs[table_no] = self.table_costs.get(table_no, 0) + self.order_price
                    self.earlyses_reserved_tables.append(table_no)
                else:
                    print(f"Table {table_no} Already Occupied for early session")
            
            elif Session == 2:
                table_no = int(input(" Enter Table Number: "))
                if table_no not in self.lateses_reserved_tables:
                    table = self.lateses_tables[table_no]
                    order_item = input("Enter the Item: ")
                    while order_item != "0":
                        p = int(input("Enter Portion: "))
                        self.lateses_order_items[order_item] = p
                        order_item = input("Enter the Item: ")

                    for item in self.lateses_order_items.keys():
                        if item in ["Lobster", "Steak Diane"]:
                            self.priority_orders.append(item)
                

                        self.order_price += self.menu.items[item] * self.lateses_order_items[item]
                        self.menu.menu_popularity[item] += 1
                    table["orders"].update(self.lateses_order_items)
                    table["Session"] = "Late Session"

                    tip = 0.05 * self.order_price
                    
                    if len(self.lateses_order_items) != 0:
                        print("Select Payment Method")
                        payment_methods = ["1.Pay with Visa/Master Card", "2. Pay with Cash"]
                        for i in range(len(payment_methods)):
                            print(payment_methods[i])
                        pay_method = int(input("Enter Payment Method: ")) 
                        if pay_method == 1:
                            self.order_price += self.order_price * 0.1
                        
                        print("Table Reserved Successfully")
                        table["status"] = "Occupied"
                        table["Number of guests"] = no_guest
                        table["cost"] = f"${self.order_price}"

                    self.total_income += self.order_price
                    self.total_tips += tip
                    self.table_costs[table_no] = self.table_costs.get(table_no, 0) + self.order_price
                    self.lateses_reserved_tables.append(table_no)
                else:
                    print(f"Table {table_number} Already Occupied for late session ")

            else:
                print("Invalid Session. Please Try Again!!!")
        else:
            print("Only 8 guests are allowed to sit for a table")
            
 # Method to display total income and tips collected.
    def income(self):
        print(f"Total Income: ${self.total_income}")
        print(f"Total Tips collected : ${self.total_tips}")

 # Method to display the status of restaurant tables.
    def table_status(self):
         print("Early Session Tables ")
         for i in range(1, 6):
            print("Table", i, self.earlyses_tables[i])
        
         print("Late Session Tables ")
         for i in range(1, 6):
            print("Table", i, self.lateses_tables[i])

         max_table = max(self.table_costs, key=self.table_costs.get)
         print(f"Table {max_table} has the highest cost: ${self.table_costs[max_table]}")

 # Method to display menu item popularity.
    def popularity(self):
        popularity = sorted(self.menu.menu_popularity.items(), key=lambda x: x[1], reverse=True)
        for item, count in popularity:
            print(f"{item}: {count} orders")
            
 # Method for adding beverages to an order.
    def beverages(self):
      try:
        sessions = ["1. Early Session", "2. Late session"]
        for i in range(len(sessions)):
            print(sessions[i])
        sess = int(input("Session: "))
        if (sess == 1):
            print(f"Early Session Occupied Tables: {self.earlyses_reserved_tables}")
            table_num = int(input("Enter Table Number: "))
            if table_num in self.earlyses_reserved_tables:
                p = int(input("Enter Portion: "))
                self.earlyses_order_items["Beverages"] = p
                table["orders"].update(self.earlyses_order_items)
                print("Drinks Successfully Added")
            else:
                print("Table is not reserved yet")
        
        elif (sess == 2):
            print(f"Late Session Reserved tables: {self.lateses_reserved_tables}")
            table_num = int(input("Enter Table Number: "))
            if table_num in self.lateses_reserved_tables:
                p = int(input("Enter Portion: "))
                self.lateses_order_items["Beverages"] = p
                table["orders"].update(self.lateses_order_items)
                print("Drinks Successfully Added")
            else:
                print("Table is not reserved yet")
        else:
            print("Invalid Session. Please try again!!!")
      except Exception as e:
          print("An Error Occurred")

 # Main loop for running the restaurant program.    
    def run(self):
        while True:
            print("Welcome to Luccio Carlo's Restaurant")
            options = ["1. Reserve a Table", "2. Tables Availability",
                       "3. Total Income + Tips Collected",
                       "4. Menu Popularity", "5. Drinks", "6. Quiet"]

            for i in range(len(options)):
                print(options[i])
                
            opt = str(input("Choose Option: "))
            if opt == "1":
                print("Reserve a Table")
                self.place_order()
            elif opt == "2":
                print("Tables Availability")
                self.table_status()
            elif opt == "3":
                print("Total Income + tips Collected")
                self.income()
            elif opt == "4":
                print("Menu Popularity")
                self.popularity()
            elif opt == "5":
                print("Alcoholic or non-alcoholic beverages")
                self.beverages()
            elif opt == "6":
                exit()      
            else:    
                print("Invalid Option. Please Try Again!!!")

       
           
                
# Entry point for the program.
if __name__ == "__main__":
    restaurant = Program()
    restaurant.run()

